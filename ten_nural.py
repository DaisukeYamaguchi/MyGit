import tensorflow as tf
import random

input_size = 30
hidden_size = 500
label_size = 8
rate = 0.0001
iteration = 20000
samle = 100
check = 2000

# 入力データ（300次元の文書データ）
x = tf.placeholder(tf.float32, [None, input_size])
# 正解ラベル（文書カテゴリのOne Hotベクトル）
y_ = tf.placeholder(tf.float32, [None, label_size])

# 隠れ層のWeight
W_h = tf.Variable(tf.random_normal([input_size, hidden_size], mean=0.0, stddev=0.05))
# 出力層のWeight
W_o = tf.Variable(tf.random_normal([hidden_size, label_size], mean=0.0, stddev=0.05))
# 隠れ層のバイアス
b_h = tf.Variable(tf.zeros([hidden_size]))
# 出力層のバイアス
b_o = tf.Variable(tf.zeros([label_size]))

# 隠れ層（シグモイド関数）
h = tf.sigmoid(tf.matmul(x, W_h) + b_h)
# 出力層（ソフトマックス）
y = tf.nn.softmax(tf.matmul(h, W_o) + b_o)

# 交差エントロピー
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# 正則化（Regularization）
l2 = tf.nn.l2_loss(W_h) + tf.nn.l2_loss(W_o)
l2_lambda = 0.01 
# コスト関数
loss = cross_entropy + l2_lambda * l2

# 勾配降下法により最適解を見つける
train_step = tf.train.GradientDescentOptimizer(rate).minimize(loss)

# 結果チェック（yとy_がイコールの場合True、異なる場合Falseとなるようなリストを作成）
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 正解率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



# TensorFlowの変数の初期化
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

print("START TRAINING")

# トレーニング（20000回のイテレーション）
for i in range(iteration):
    # training_xyは、事前準備しておいた学習用データ（文書ベクトルとラベルがタプルで入っているリスト）
    # ミニバッチ（100件ランダムで取得）
    samples = random.sample(training_xy, samle)
    batch_xs = [s[0] for s in samples]
    batch_ys = [s[1] for s in samples]
    # 確率的勾配降下法を使い最適なパラメータを求める
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    # 2000回毎に正解率を確認
    if i % check == 0:
        a = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys})
        print("TRAINING(%d): %.0f%%" % (i, (a * 100.0)))
    



# テストデータで正解率を確認
# test_x, test_yは事前準備しておいたテストデータ
a = sess.run(accuracy, feed_dict={x: test_x, y_: test_y})
print("TEST DATA ACCURACY: %.0f%%" % (a * 100.0))