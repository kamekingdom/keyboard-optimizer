# ChatGPTより頻出単語500を生成
words_list = [
    "の", "に", "は", "を", "た", "が", "で", "て", "と", "し",
    "れ", "さ", "ある", "こと", "たり", "する", "ない", "も", "な",
    "いる", "か", "あっ", "ん", "なる", "たい", "する", "べき", "なっ",
    "なく", "たり", "い", "ず", "ぬ", "だ", "なん", "くる", "あいつ",
    "どれ", "し", "って", "き", "や", "てる", "いい", "なら", "いく",
    "う", "まし", "あの", "あれ", "みたい", "かな", "あり", "くれ", "やつ",
    "られ", "たち", "み", "ね", "れる", "とか", "なく", "うん", "よ",
    "もの", "かも", "んじゃ", "ら", "え", "じゃ", "わ", "には", "だけ",
    "とい", "けど", "ほしい", "ている", "てい", "せ", "ひと", "ここ", "させ",
    "ながら", "これ", "にな", "のに", "なんて", "かけ", "あるい", "とき",
    "まで", "という", "なかっ", "られる", "ほう", "とき", "だっ", "できる",
    "それ", "しま", "しまっ", "どう", "あと", "ええ", "だい", "せる",
    "ねえ", "てき", "ずつ", "てみ", "いま", "えええ", "ねぇ", "られる",
    "ありま", "だって", "ねー", "だろ", "おまえ", "たら", "っ", "ば",
    "んだ", "ほんと", "かなり", "んだけど", "やる", "だけど", "くらい",
    "あるか", "すごい", "だけで", "なかなか", "ちゃん", "ながらも", "くらい",
    "なくて", "おい", "だいぶ", "ないか", "こそ", "やっ", "さすが", "でしょ",
    "なかなか", "たくさん", "さえ", "かなぁ", "わかる", "なるほど", "ってる",
    "かい", "しな", "わり", "そういう", "ため", "どっち", "お前", "おかしい",
    "うち", "しまい", "だけれ", "とりあえず", "ついて", "なお", "もう少し",
    "なれ", "あとで", "まじ", "ちゃう", "まっ", "たちまち", "にも", "すごく",
    "どこ", "すら", "もうちょっと", "なに", "つもり", "やっぱり", "までに",
    "つけ", "でも", "だけど", "とっくに", "なにか", "いくつか", "なにも",
    "しばらく", "いただ", "くらいの", "いくら", "までの", "しまえ", "たりとも",
    "でも", "せい", "あそこ", "もっと", "ついては", "せいか", "しまえば",
    "すぎる", "からか", "せいな", "いえ", "とも", "なし", "でもない",
    "なり", "しろ", "とかいう", "ねば", "すれ", "はい", "いいえ", "させる",
    "みた", "ねぇねぇ", "かなり", "わたし", "させて", "どうか", "にもかかわらず",
    "まい", "はな", "つか", "られな", "みんな", "あなた", "しても", "なれる",
    "しても", "なんていう", "つつ", "まいと", "とかで", "てな", "さす", "だめ",
    "してい", "すると", "べく", "られない", "まいとして", "しながら",
    "ために", "させた", "さえも", "しては", "かまわ", "なくせ", "からといって",
    "だろう", "でい", "ひとり", "つける", "ておいて", "しく", "かなん",
    "とっとと", "ために", "なんて", "だから", "ので", "られなく", "しそう",
    "たいと", "てきた", "あった", "でしょう", "もら", "ていた", "からな",
    "とりま", "だった", "にし", "てみた", "すでに", "だけども", "あたり",
    "みて", "じゃな", "といった", "ないし", "までには", "ためには", "だらけ",
    "けれど", "たこと", "でもある", "ずに", "だろうか", "だらけの", "てるか",
    "といったら", "について", "らしい", "もん", "にとって", "てしまった",
    "からと言って", "でしか", "のみ", "さえない", "からすると", "のみならず",
    "といわず", "である", "かと", "ばかり", "だけれども", "というのも",
    "たらしめる", "ずには", "つもりで", "しか", "てまい", "たりする",
    "ことの", "とかで", "ずみ", "てこそ", "からすると", "にもならない",
    "たりすること", "だっていう", "とかない", "くせ", "のには", "とかの",
    "ばかりの", "てたり", "にしろ", "のでは", "ていい", "からいって",
    "てまえ", "たりという", "でもなく", "かない", "たりない", "しかない",
    "によると", "によって", "てから", "たばかり", "にしよう", "のみか",
    "にしろ", "てんだ", "ていか", "てない", "によっては", "かというと",
    "かといって", "からの", "にあたる", "でいける", "からの", "がち",
    "からだ", "からの", "からなく", "てもいい", "かの", "にしようと",
    "とかの", "でもないか", "たりする", "ていって", "ないかな",
    "かもしれない", "にはならない", "たいだけ", "てんだが", "ないだけ",
    "たいたい", "かもしれ", "てきたり", "ないから", "たいこと", "たいのに",
    "てて", "かのよう", "によるのは", "でたり", "たりのは", "たいし",
    "ないかと", "かけて", "かけたり", "ともの", "からすれば",
    "たりだ", "ってのは", "たりすると", "たいてい", "としても",
    "ないかなぁ", "ないん", "において", "かたがた", "かけれ", "ずのは",
    "といっても", "てさえ", "かけた", "なくも", "なくした", "たくと",
    "とともに", "における", "もらえ", "てきたり", "ついたり", "かのような",
    "にあたり", "たりながら", "からの", "にあたって", "てるだけ",
    "できるか", "かのように", "ているか", "ともだち", "てほしい",
    "てある", "ずにも", "かしら", "であろう", "ているん", "かもしれ",
    "からといった", "ともだち", "ないに", "ていく", "ないこと",
    "かもしれないけど", "たとえば", "かと言って", "にいたって", "けれども",
    "かというと", "たことの", "ずにはいられ", "かけると", "くらいのこと",
    "ないもの", "っていたり", "においても", "ものだ", "ずにはいられない",
    "かというと", "かけたりする", "くせに", "における", "においての",
    "たっていう", "とすると", "により", "ているよ", "によるのが",
    "かければ", "ずつの", "くせして", "だいたいの", "とし", "といえば",
    "かのう", "かけるのは", "かけるのは", "からといっても",
    "くせしても", "くせしても", "ずにはおかない", "からのには", "なかったこと",
    "かもしれません", "かけるので", "くせには", "くせにも", "さらには",
    "してくれる", "つけたり", "てもの", "たいとしても",
    "たりするのが", "たりするのが", "といっても", "ないかと思", "ないでしょ",
    "かもしれないし", "ているという", "といえる", "とはい", "なかったという",
    "かけたい", "かけたい", "かけること", "からはじまり", "くせになる",
    "てはじめて", "であること", "とともに", "なかったり", "なんだか",
    "にはない", "においても", "のだけ", "ずつかり", "ともなって",
    "ていくこと", "ているのは", "とはいえ", "ないしょ", "のもの",
    "によるもの", "のものだ", "ずつのこと", "からはじまっ", "けれど",
    "くせにはい", "だってば", "たいのか", "たりすることが",
    "ともなると", "ながらもの", "なくもの", "ぬきで", "ねたら", "ねらい",
    "ねらいで", "までのこと", "ものでも", "よねぇ", "りません",
    "りませんか", "りませんかね", "りましょうか", "りましょうかね",
    "るのだろう", "れるので", "れるのは", "ろうか", "わりには",
    "わりにも", "んです", "んですか", "んですかね", "んですけど",
    "んですけどね", "んですよ", "んですよね", "んでしょう",
    "んでしょうか", "んでしょうかね", "んでしょうね"
]

import re
import MeCab
import pykakasi

def extract_hiragana(text):
    hiragana_pattern = r"[\u3040-\u309Fー]+"
    hiragana_list = re.findall(hiragana_pattern, text)
    extracted_text = " ".join(hiragana_list)
    return extracted_text

def hiragana_to_romaji(hiragana_text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('H', 'a')  # ひらがなをローマ字に変換する設定
    conv = kakasi.getConverter()
    romaji_text = conv.do(hiragana_text)
    return romaji_text

def extract_words(text):
    mecab = MeCab.Tagger("-Owakati")  # 分かち書きの形式で出力
    parsed = mecab.parse(text)
    words = parsed.strip().split(" ")
    return words

def count_word_frequency(words):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    return word_freq

words_string = ""
for word in words_list:
    words_string += f" {word}"

hiragana_words = extract_hiragana(words_string)

romaji_words = hiragana_to_romaji(hiragana_words)
# print(romaji_words)

# 結果
input_text = "no ni ha wo ta ga de te to shi re sa aru koto tari suru nai mo na iru ka atsu n naru tai suru beki natsu naku tari i zu nu da nan kuru aitsu dore shi tte ki ya teru ii nara iku u mashi ano are mitai kana ari kure yatsu rare tachi mi ne reru toka naku un yo mono kamo nja ra e ja wa niha dake toi kedo hoshii teiru tei se hito koko sase nagara kore nina noni nante kake arui toki made toiu nakatsu rareru hou toki datsu dekiru sore shima shimatsu dou ato ee dai seru nee teki zutsu temi ima eee nee rareru arima datte nee daro omae tara tsu ba nda honto kanari ndakedo yaru dakedo kurai aruka sugoi dakede nakanaka chan nagaramo kurai nakute oi daibu naika koso yatsu sasuga desho nakanaka takusan sae kanaa wakaru naruhodo tteru kai shina wari souiu tame dotchi o okashii uchi shimai dakere toriaezu tsuite nao mou shi nare atode maji chau matsu tachimachi nimo sugoku doko sura mouchotto nani tsumori yappari madeni tsuke demo dakedo tokkuni nanika ikutsuka nanimo shibaraku itada kuraino ikura madeno shimae taritomo demo sei asoko motto tsuiteha seika shimaeba sugiru karaka seina ie tomo nashi demonai nari shiro tokaiu neba sure hai iie saseru mita neenee kanari watashi sasete douka nimokakawarazu mai hana tsuka rarena minna anata shitemo nareru shitemo nanteiu tsutsu maito tokade tena sasu dame shitei suruto beku rarenai maitoshite shinagara tameni saseta saemo shiteha kamawa nakuse karatoitte darou dei hitori tsukeru teoite shiku kanan tottoto tameni nante dakara node rarenaku shisou taito tekita atta deshou mora teita karana torima datta nishi temita sudeni dakedomo atari mite jana toitta naishi madeniha tameniha darake keredo takoto demoaru zuni darouka darakeno teruka toittara nitsuite rashii mon nitotte teshimatta karato tte deshika nomi saenai karasuruto nominarazu toiwazu dearu kato bakari dakeredomo toiunomo tarashimeru zuniha tsumoride shika temai tarisuru kotono tokade zumi tekoso karasuruto nimonaranai tarisurukoto datteiu tokanai kuse noniha tokano bakarino tetari nishiro nodeha teii karaitte temae taritoiu demonaku kanai tarinai shikanai niyoruto niyotte tekara tabakari nishiyou nomika nishiro tenda teika tenai niyotteha katoiuto katoitte karano niataru deikeru karano gachi karada karano karanaku temoii kano nishiyouto tokano demonaika tarisuru teitte naikana kamoshirenai nihanaranai taidake tendaga naidake taitai kamoshire tekitari naikara taikoto tainoni tete kanoyou niyorunoha detari tarinoha taishi naikato kakete kaketari tomono karasureba tarida ttenoha tarisuruto taitei toshitemo naikanaa nain nioite katagata kakere zunoha toittemo tesae kaketa nakumo nakushita takuto totomoni niokeru morae tekitari tsuitari kanoyouna niatari tarinagara karano niatatte terudake dekiruka kanoyouni teiruka tomodachi tehoshii tearu zunimo kashira dearou teirun kamoshire karatoitta tomodachi naini dake zutsukari tomonatte teikukoto teirunoha tohaie naisho nomono niyorumono nomonoda zutsunokoto karahajimatsu keredo kusenihai datteba tainoka tarisurukotoga tomonaruto nagaramono nakumono nukide netara nerai neraide madenokoto monodemo yonee rimasen rimasenka rimasenkane rimashouka rimashoukane runodarou rerunode rerunoha rouka wariniha warinimo ndesu ndesuka ndesukane ndesukedo ndesukedone ndesuyo ndesuyone ndeshou ndeshouka ndeshoukane ndeshoune"

# 単語の出現頻度を数える
# word_freq = count_word_frequency(words)

# 頻出上位500個の単語を選ぶ
# top_500_words = sorted(word_freq, key=word_freq.get, reverse=True)[:500]

# print(top_500_words)
