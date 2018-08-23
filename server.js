var exec = require('child_process').exec;

/*
var big5 = {
  "big5_openness": {"label": "知的好奇心", "explain": "経験への開放性。高い人： 知的好奇心があり、落ち着きがあり、美に敏感で、新しいことを試そうとするタイプです。低い人： 平穏を好み、率直で、複雑なものや曖昧なもの、取るに足らないものに対して関心を持たないタイプです。"},
  "big5_conscientiousness": {"label": "誠実性", "explain": "高い人： 自己統制をし、誠実、あるいは外部の期待や評価に応えようとするタイプです。低い人： 計画に従うより、自発的に物事を行うことを好むタイプです。"},
  "big5_extraversion": {"label": "外向性", "explain": "高い人： よりエネルギッシュで、社交的なタイプです。グループ内で目立つこと、話しをすること、自分を主張することが好きです。低い人： 刺激をあまり求めず、人とのかかわりを避けるタイプです。但しそれは、臆病、非友好的、反社会的であるということではありません。"},
  "big5_agreeableness": {"label": "協調性", "explain": "高い人： 他人とうまくやっていくことを重要視するタイプです。人間の本性に関して楽観的な見方をしています。低い人： 他人より自分の興味を優先するタイプです。 他人の言葉の裏を考えてしまう傾向があります。"},
  "big5_neuroticism": {"label": "神経症傾向", "explain": "高い人： 否定的な感情を抱いたり、取り乱したりするタイプです。それは、苦労が多いことを意味しているのかも知れません。低い人： 穏やかで、あまり怒らないタイプです。 但し、それは、自信に満ちていたり幸せな人だというわけではありません。"},
  "facet_adventurousness": {"label": "冒険", "explain": "新しい活動に挑戦し、新しいことを経験しようとする意欲。"},
  "facet_artistic_interests": {"label": "芸術的興味", "explain": "人工物か自然物かにかかわらない、芸術と美の評価。"},
  "facet_emotionality": {"label": "", "explain": "情緒的応答性;自分の感情についての認識。"},
  "facet_imagination": {"label": "", "explain": "内面で空想の世界を作り出すことへの寛容性。"},
  "facet_intellect": {"label": "", "explain": "知的好奇心;新しいアイディアへの寛容さ。"},
  "facet_liberalism": {"label": "", "explain": "自分の価値観と慣習を再検討する寛容さ;権威に挑戦する覚悟。"},
  "facet_achievement_striving": {"label": "", "explain": "個人的な成功の必要性と方向感。"},
  "facet_cautiousness": {"label": "", "explain": "行動したり話したりする前に物事を考える傾向。"},
  "facet_dutifulness": {"label": "", "explain": "義務感;義務を果たすことを重要視する度合い。"},
  "facet_orderliness": {"label": "", "explain": "個人的秩序、整理、整頓。"},
  "facet_self_discipline": {"label": "", "explain": "自制心;いったん仕事を始めると退屈だったり気が散ったりするのを我慢して最後までやり遂げる能力。"},
  "facet_self_efficacy": {"label": "", "explain": "自分の能力への信念。"},
  "facet_activity_level": {"label": "", "explain": "生活のペース;忙しさのレベル。"},
  "facet_assertiveness": {"label": "", "explain": "主張の力強さ;リーダーシップと社会的支配への志向性;他人の活動を指示したいという願望。"},
  "facet_cheerfulness": {"label": "", "explain": "ポジティブな気持ちを感じたり、表現したりする傾向。"},
  "facet_excitement_seeking": {"label": "", "explain": "環境的刺激への欲求。"},
  "facet_friendliness": {"label": "", "explain": "他人に対する興味と友情;人付き合いへの自信。"},
  "facet_gregariousness": {"label": "", "explain": "他の仲間に対する好意;社交性の高さ。"},
  "facet_altruism": {"label": "", "explain": "他人の福利に純粋な関心を抱きそのために活動しようという気持ち。"},
  "facet_cooperation": {"label": "", "explain": "対立への嫌悪。対人関係での争いに対して妥協して解決しようとする姿勢。"},
  "facet_modesty": {"label": "", "explain": "控えめで成果を前面に出さない傾向;謙遜。"},
  "facet_morality": {"label": "", "explain": "表現における率直さと純粋さ; 遠慮がなく、ぶっきらぼう。"},
  "facet_sympathy": {"label": "", "explain": "他人への思いやりの態度。親切さ。"},
  "facet_trust": {"label": "", "explain": "他人から誠実さと善意に対して信頼されている度合い。"},
  "facet_anger": {"label": "激情的", "explain": "怒りや不満を表現しないまでも経験する傾向。"},
  "facet_anxiety": {"label": "心配性", "explain": "困難なことやトラブルにこだわる傾向;不安や懸念を抱えやすい。"},
  "facet_depression": {"label": "悲観的", "explain": "罪悪感、悲しみ、絶望、または孤独の感情を抱きやすい傾向。 "},
  "facet_immoderation": {"label": "利己的", "explain": "欲望と衝動を抑えたり遅らせたりするよりも、それらのままに行動する傾向。"},
  "facet_self_consciousness": {"label": "自意識過剰", "explain": "拒絶と当惑に関する関心;内気。"},
  "facet_vulnerability": {"label": "低ストレス耐性", "explain": "困難な状況でのストレスや圧力への対処の困難さ。"},
  "need_structure": {"label": "仕組", "explain": "明確な目的を持っている組織、計画、および物事の必要性。"},
  "need_stability": {"label": "安定性", "explain": "優れた実績と知られた経歴を持つ、思慮、実証、及び検査の必要性"},
  "need_self_expression": {"label": "自己表現", "explain": "自分のアイデンティティを発見し、主張する欲望。"},
  "need_practicality": {"label": "実用主義", "explain": "仕事をこなし、技量、効率を求める欲望。"},
  "need_love": {"label": "社会性", "explain": "一対一、一体多かによらない、社会との接触。"},
  "need_liberty": {"label": "自由主義", "explain": "逃亡の必要性、新しい経験や新しいものに対する欲望。"},
  "need_ideal": {"label": "理想", "explain": "しばしば共同体意識の追求として見られる、生活や経験における完全性のアイディアに対する欲求。"},
  "need_harmony": {"label": "調和", "explain": "他人、彼らの見解、及びおよび感覚を高く評価したり喜ばせる必要性。"},
  "need_excitement": {"label": "興奮", "explain": "熱意と意欲をそそる経験を追求したり生活を送る必要性。"},
  "need_curiosity": {"label": "好奇心", "explain": "学習、探求心、および成長を促進する経験を追求する必要性。"},
  "need_closeness": {"label": "親密", "explain": "はぐくみ、はぐくまれる必要性;所属感。"},
  "need_challenge": {"label": "挑戦", "explain": "達成、成功、競争、または自分の能力を試す経験を追求する欲望。"},
  "value_conservation": {"label": "現状維持", "explain": "文化や宗教の違いによる習慣やアイディアに対する尊敬、約束、および受け入れ。"},
  "value_openness_to_change": {"label": "変化許容性", "explain": "生活における興奮、新規性、および挑戦。"},
  "value_hedonism": {"label": "快楽主義", "explain": "自分自身のための喜びや感覚的な満足感。"},
  "value_self_enhancement": {"label": "自己増進", "explain": "社会的な基準に基づいて能力を実証することによる個人的な成功。"},
  "value_self_transcendence": {"label": "自己超越", "explain": "頻繁に接触を行っている人の幸せを維持し向上すること。"}
}
*/

var big5 = {
  "Openness": {"label": "知的好奇心", "explain": "経験への開放性。高い人： 知的好奇心があり、落ち着きがあり、美に敏感で、新しいことを試そうとするタイプです。低い人： 平穏を好み、率直で、複雑なものや曖昧なもの、取るに足らないものに対して関心を持たないタイプです。"},
  "Conscientiousness": {"label": "誠実性", "explain": "高い人： 自己統制をし、誠実、あるいは外部の期待や評価に応えようとするタイプです。低い人： 計画に従うより、自発的に物事を行うことを好むタイプです。"},
  "Extraversion": {"label": "外向性", "explain": "高い人： よりエネルギッシュで、社交的なタイプです。グループ内で目立つこと、話しをすること、自分を主張することが好きです。低い人： 刺激をあまり求めず、人とのかかわりを避けるタイプです。但しそれは、臆病、非友好的、反社会的であるということではありません。"},
  "Agreeableness": {"label": "協調性", "explain": "高い人： 他人とうまくやっていくことを重要視するタイプです。人間の本性に関して楽観的な見方をしています。低い人： 他人より自分の興味を優先するタイプです。 他人の言葉の裏を考えてしまう傾向があります。"},
  "Emotional range": {"label": "神経症傾向", "explain": "高い人： 否定的な感情を抱いたり、取り乱したりするタイプです。それは、苦労が多いことを意味しているのかも知れません。低い人： 穏やかで、あまり怒らないタイプです。 但し、それは、自信に満ちていたり幸せな人だというわけではありません。"}
}

exec('curl -X POST -u d45e68c1-99e6-40a2-9e0e-eeff70bfc622:omm2050pAWQS --header "Content-Type: application/json" --header "Accept: application/json" --data-binary @profile.json "https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2017-10-13&consumption_preferences=true&raw_scores=true"', (err, stdout, stderr) => {
  if(err){
    console.log(err);
  }
  var json = JSON.parse(stdout);
  big5['Openness']['percentile'] = json.personality[0].percentile
  big5['Conscientiousness']['percentile'] = json.personality[1].percentile
  big5['Extraversion']['percentile'] = json.personality[2].percentile
  big5['Agreeableness']['percentile'] = json.personality[3].percentile
  big5['Emotional range']['percentile'] = json.personality[4].percentile
  console.log(big5);
});
