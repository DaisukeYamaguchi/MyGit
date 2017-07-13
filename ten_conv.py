models = {
    # ファイル名で当該文書の行列が取得できるようにする
    'it-life-hack-6292880.txt':[
        [-2.27736831e-01,  -6.95074769e-03,...], # 旧式
        [1.1219008 , -2.06810808,...],           # Mac
        [-0.07440117, -1.02441812,...],          # で
        [0.21738884,  0.46838179,...],           # 禁断
        [6.83333278e-02, 6.72825038e-01,...],    # の
        [-0.12795788,  0.58305722,...]           # パワーアップ
        ...
        [0.0, 0.0, ...] # 未知語もしくは500単語以内の文章は0ベクトルでパディング
    ],
    'it-life-hack-6294340.txt':[
        ...
    ],
    ...
}



import tensorflow as tf
 
# 定数
# 単語ベクトルのサイズ
EMBEDDING_SIZE = 100
# １フィルター種類に対するフィルターの個数
FILTER_NUM = 128
# 1文書に含まれる単語数（全文書合わせてある）
DOCUMENT_LENGTH = 500
# ドキュメントクラス
DOC_CLASS_DEF = [
    'dokujo-tsushin',
    'it-life-hack',
    'kaden-channel',
    'livedoor-homme',
    'movie-enter',
    'peachy',
    'smax',
    'sports-watch',
    'topic-news',
]

# 変数
# インプット変数（各文書が500 x 100のマトリクス）
x = tf.placeholder(tf.float32, [None, DOCUMENT_LENGTH, EMBEDDING_SIZE], name="x")
# アプトプット変数（文書カテゴリー）
y_ = tf.placeholder(tf.float32, [None, len(DOC_CLASS_DEF)], name="y_")
# ドロップアウト変数
dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

# インプット変数の次元を拡張しておく（channel）
x_expanded = tf.expand_dims(x, -1)



# フィルタサイズ：3単語、4単語、5単語の３種類のフィルタ
filter_sizes = [3, 4, 5]
# 各フィルタ処理結果をMax-poolingした値をアペンドしていく
pooled_outputs = []
for i, filter_size in enumerate(filter_sizes):
    # フィルタのサイズ（単語数, エンベディングサイズ、チャネル数、フィルタ数）
    filter_shape = [filter_size, EMBEDDING_SIZE, 1, FILTER_NUM]
    # フィルタの重み、バイアス
    W_f = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
    b_f = tf.Variable(tf.constant(0.1, shape=[FILTER_NUM]), name="b")
    # Tensorflowの畳み込み処理
    conv = tf.nn.conv2d(
        x_expanded,
        W_f,
        strides=[1, 1, 1, 1],
        padding="VALID",
        name="conv"
    )
    # 活性化関数にはReLU関数を利用
    h = tf.nn.relu(tf.nn.bias_add(conv, b_f), name="relu")
    # プーリング層 Max Pooling
    pooled = tf.nn.max_pool(
        h,
        ksize=[1, DOCUMENT_LENGTH - filter_size + 1, 1, 1],
        strides=[1, 1, 1, 1],
        padding="VALID",
        name="pool"
    )
    pooled_outputs.append(pooled)

# プーリング層の結果をつなげる
filter_num_total = FILTER_NUM * len(filter_sizes)
h_pool = tf.concat(3, pooled_outputs)
h_pool_flat = tf.reshape(h_pool, [-1, filter_num_total])



# ドロップアウト（トレーニング時0.5、テスト時1.0）
h_drop = tf.nn.dropout(h_pool_flat, dropout_keep_prob)

# アウトプット層
class_num = len(DOC_CLASS_DEF)
W_o = tf.Variable(tf.truncated_normal([filter_num_total, class_num], stddev=0.1), name="W")
b_o = tf.Variable(tf.constant(0.1, shape=[class_num]), name="b")
scores = tf.nn.xw_plus_b(h_drop, W_o, b_o, name="scores")
predictions = tf.argmax(scores, 1, name="predictions")



# コスト関数（交差エントロピー）
losses = tf.nn.softmax_cross_entropy_with_logits(scores, y_)
loss = tf.reduce_mean(losses)

# 正答率
correct_predictions = tf.equal(predictions, tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")

# Adamオプティマイザーによるパラメータの最適化
global_step = tf.Variable(0, name="global_step", trainable=False)
optimizer = tf.train.AdamOptimizer(1e-4)
grads_and_vars = optimizer.compute_gradients(loss)
train_step = optimizer.apply_gradients(grads_and_vars, global_step=global_s



# 各テンソルのイニシャライズ
init = tf.initialize_all_variables()
 
sess = tf.Session()
sess.run(init)

# 14000回のイテレーション
for i in range(14000):
    # ミニバッチ（100件ランダムで取得）
    # training_xyには、modelsで定義した各文書行列及び正解ラベル（カテゴリ）が入っている
    samples = random.sample(training_xy, 100)
    batch_xs = [s[0] for s in samples]
    batch_ys = [s[1] for s in samples]
    # 確率的勾配降下法を使い最適なパラメータを求める
    # dropout_keep_probは0.5を指定
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys, dropout_keep_prob: 0.5})
    if i % 100 == 0:
        # 100件毎に正答率を表示
        a = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys, dropout_keep_prob: 0.5})
        print("TRAINING(%d): %.0f%%" % (i, (a * 100.0)))
    

# テストデータの正答率
a = sess.run(accuracy, feed_dict={x: test_x, y_: test_y, dropout_keep_prob: 1.0})
print("TEST DATA ACCURACY: %.0f%%" % (a * 100.0))

