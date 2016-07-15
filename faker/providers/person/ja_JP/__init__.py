# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{last_name}} {{first_name_female}}',
    )

    formats_male = (
        '{{last_name}} {{first_name_male}}',
    )

    formats = formats_male + formats_female

    first_names_female = (
        'あきら', '明美', 'あすか', '香織', '加奈', 'くみ子', 'さゆり', '千代', '翼', '知実',
        '直子', '七夏', '花子', '春香', '真綾', '舞', '幹', '桃子', '結衣', '陽子', '裕美子', '零', '里佳',
    )

    first_names_male = (
        '晃', '篤司', '治', '京助', '健一', '淳', '聡太郎', '太一', '拓真', '太郎', '翼', '智也',
        '直樹', '直人', '英樹', '浩', '学', '充', '稔', '裕樹', '裕太', '康弘', '陽一', '洋介', '亮介', '涼平',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        '青田', '青山', '石田', '井高', '伊藤', '井上', '宇野', '江古田', '大垣',
        '加藤', '加納', '喜嶋', '木村', '桐山', '工藤', '小泉', '小林', '近藤',
        '斉藤', '坂本', '佐々木', '佐藤', '笹田', '鈴木', '杉山',
        '高橋', '田中', '田辺', '津田',
        '中島', '中村', '渚', '中津川', '西之園', '野村',
        '原田', '浜田', '廣川', '藤本',
        '松本', '三宅', '宮沢', '村山',
        '山岸', '山口', '山田', '山本', '吉田', '吉本',
        '若松', '渡辺',
        "田井", "大恩", "大学", "大工屋", "太期", "大後", "醍醐", "大胡", "大光", "大郷", "大幸", "大光寺", "大黒", "大黒谷", "太皷地",
        "大悟法", "大座", "泰山", "大司", "大蛇森", "大刕", "第十", "太寿堂", "大條", "大上", "大上戸",
        "大正水流", "第新", "大豆本", "大善", "泰田", "紿田", "代田", "代々", "大代", "大長", "大戸", "大塔", "大道", "帯刀", "大藤", "大洞",
        "大導寺", "大道寺", "大徳寺", "対中", "胎内", "田井中", "對中", "大成", "大日", "田結庄",
        "台信", "大悲山", "大符", "大部", "題佛", "大保", "大坊", "大宝寺", "当麻", "台丸谷", "大毛", "大陽", "平葭", "多比良", "泰良", "平等", "平良",
        "大良", "平楽", "平久", "大楽", "平舘", "大六野", "多宇", "田内", "妙中",
        "妙楽", "田尾田", "垰田", "垰野", "垰畑", "垰村", "田面", "峠本", "多加", "多賀", "田賀", "駄賀", "高荒", "互井", "田貝", "高礒", "高市", "多賀糸",
        "田垣内", "高稲", "高氏", "高馬", "高江洲", "高江洌", "高榎", "鷹尾", "高岳",
        "高丘", "高生加", "高落", "高柿", "高笠", "隆紀", "高来", "鷹木", "鷹来", "都木", "堯木", "高久", "高草木", "高楠", "高久田", "大下倉", "高鍬", "高子",
        "高桜", "高司", "高士", "高志", "隆志", "高師", "高茂", "高下", "高實子",
        "高科", "高階", "孝島", "鷹島", "高清水", "高庄", "田頭", "鷹巣", "鷹栖", "高須賀", "隆杉", "高数後", "高砂", "高世", "高清", "堯勢", "高宗", "高僧", "高惣",
        "鷹左右", "高袖", "高他", "高多", "田形", "高舘", "高玉", "高地"

    )

    kana_formats = (
        '{{last_kana_name}} {{first_kana_name_female}}',
        '{{last_kana_name}} {{first_kana_name_male}}',
    )

    first_kana_names_female = (
        'アキラ', 'アケミ', 'アスカ',
        'カオリ', 'カナ', 'クミコ',
        'サユリ',
        'チヨ', 'ツバサ', 'トモミ',
        'ナオコ', 'ナナカ',
        'ハナコ', 'ハルカ',
        'マアヤ', 'マイ', 'ミキ', 'モモコ',
        'ユイ', 'ヨウコ', 'ユミコ',
        'レイ', 'リカ',
    )

    first_kana_names_male = (
        'アキラ', 'アツシ', 'オサム',
        'キョウスケ', 'ケンイチ',
        'ジュン', 'ソウタロウ',
        'タイチ', 'タクマ', 'タロウ', 'ツバサ', 'トモヤ',
        'ナオキ', 'ナオト',
        'ヒデキ', 'ヒロシ',
        'マナブ', 'ミツル', 'ミノル', 'ヒロキ',
        'ユウタ', 'ヤスヒロ', 'ヨウイチ', 'ヨウスケ',
        'リョウスケ', 'リョウヘイ',
    )

    first_kana_names = first_kana_names_male + first_kana_names_female

    last_kana_names = (
        'アオタ', 'アオヤマ', 'イシダ', 'イダカ', 'イトウ', 'イノウエ', 'ウノ', 'エコダ', 'オオガキ',
        'カトウ', 'カノウ', 'キジマ', 'キムラ', 'キリヤマ', 'クドウ', 'コイズミ', 'コバヤシ', 'コンドウ',
        'サイトウ', 'サカモト', 'ササキ', 'サトウ', 'ササダ', 'スズキ', 'スギヤマ',
        'タカハシ', 'タナカ', 'タナベ', 'ツダ',
        'ナカジマ', 'ナカムラ', 'ナギサ', 'ナカツガワ', 'ニシノソノ', 'ノムラ',
        'ハラダ', 'ハマダ', 'ヒロカワ', 'フジモト',
        'マツモト', 'ミヤケ', 'ミヤザワ', 'ムラヤマ',
        'ヤマギシ', 'ヤマグチ', 'ヤマダ', 'ヤマモト', 'ヨシダ', 'ヨシモト',
        'ワカマツ', 'ワタナベ',
        "タイ", "タイオン", "ダイガク", "ダイクヤ", "ダイコ", "ダイゴ", "ダイコウ", "ダイゴウ",
        "ダイコウジ", "ダイコク", "ダイコクヤ", "タイコジ", "ダイゴボウ", "ダイザ", "タイザン", "タイシ", "ダイジャモリ", "タイシュウ",
        "ダイジュウ", "ダイジュドウ", "ダイジョウ", "ダイジョウゴ", "タイショウズル", "ダイシン", "ダイズモト", "ダイゼン",
        "タイダ", "タイダ", "ダイダ", "ダイダイ", "ダイチョウ", "ダイト", "ダイトウ", "ダイドウ", "タイトウ",
        "ダイドウジ", "ダイトクジ", "タイナカ", "ダイナリ", "ダイニチ", "タイノショウ", "タイノブ",
        "ダイヒサ", "ダイフ", "ダイブ", "ダイブツ", "ダイボ", "ダイボウ", "ダイホウジ", "タイマ", "ダイマルヤ", "ダイモウ", "タイヨウ", "タイヨシ", "タイラ",
        "ダイラ", "タイラク", "ダイラク", "タイラダテ", "ダイロクノ", "タウ", "タウチ", "タエナカ", "タエラ", "タオダ",
        "タオノ", "タオハタ", "タオムラ", "タオモ", "タオモト", "タカ", "タガ", "ダガ", "タカアラ", "タガイ", "タカイソ", "タカイチ",
        "タガイト", "タカイネ", "タカウジ", "タカウマ", "タカエス", "タカエノキ", "タカオ", "タカオカ", "タカオチ",
        "タカガキ", "タカガサ", "タカキ", "タカギ", "タカク", "タカクサキ", "タカクス", "タカクタ", "タカクラ", "タカクワ",
        "タカネ", "タカザクラ", "タカシ", "タカツカサ", "タカシゲ", "タカシタ", "タカジッコ", "タカシナ", "タカシマ",
        "タカシミズ", "タカショウ", "タガシラ", "タカス", "タカスガ", "タカスギ", "タカスゴ", "タカスナ", "タカセ",
        "タカソウ", "タカソデ", "タカタ", "タガタ", "タカダテ", "タカタマ", "タカチ",

    )

    romanized_formats = (
        '{{first_romanized_name_female}} {{last_romanized_name}}',
        '{{first_romanized_name_male}} {{last_romanized_name}}',
    )

    first_romanized_names_female = (
        'Akira', 'Akemi', 'Asuka',
        'Kaori', 'Kana', 'Kumiko',
        'Sayuri',
        'Chiyo', 'Tsubasa', 'Tomomi',
        'Naoko', 'Nanaka',
        'Hanako', 'Haruka',
        'Maaya', 'Mai', 'Miki', 'Momoko',
        'Yui', 'Yoko', 'Yumiko',
        'Rei', 'Rika',
    )

    first_romanized_names_male = (
        'Akira', 'Atsushi', 'Osamu',
        'Kyosuke', 'Kenichi',
        'Jun', 'Sotaro',
        'Taichi', 'Takuma', 'Taro', 'Tsubasa', 'Tomoya',
        'Naoki', 'Naoto'
        'Hideki', 'Hiroshi',
        'Manabu', 'Mituru', 'Minoru', 'Hiroki',
        'Yuta', 'Yasuhiro', 'Yoichi', 'Yosuke',
        'Ryosuke', 'Ryohei',
    )

    first_romanized_names = first_romanized_names_male + first_romanized_names_female

    last_romanized_names = (
        'Aota', 'Aoyama', 'Ishida', 'Idaka', 'Ito', 'Inoue', 'Uno', 'Ekoda', 'Ogaki',
        'Kato', 'Kano', 'Kijima', 'Kimura', 'Kiriyama', 'Kudo', 'Koizumi', 'Kobayashi', 'Kondo',
        'Saito', 'Sakamoto', 'Sasaki', 'Sato', 'Sasada', 'Suzuki', 'Sugiyama',
        'Takahashi', 'Tanaka', 'Tanabe', 'Tsuda', 'Tsuchiya',
        'Nakajima', 'Nakamura', 'Nagisa', 'Nakatsugawa', 'Nishinosono', 'Nomura',
        'Harada', 'Hamada', 'Hirokawa', 'Fujimoto',
        'Matsumoto', 'Miyake', 'Miyagawa', 'Murayama',
        'Yamagishi', 'Yamaguchi', 'Yamada', 'Yamamoto', 'Yoshida', 'Yoshimoto',
        'Wakamatsu', 'Watanabe',
        "tai", "taion", "daigaku", "daikuya", "daiko", "daigo", "daiko", "daigo",
        "daikoji", "daikoku", "daikokuya", "taikoji", "daigobo", "daiza", "taizan", "taishi", "daijamori", "taishu",
        "daiju", "daijudo", "daijo", "daijogo", "taishozuru", "daishin", "daizumoto", "daizen",
        "taida", "taida", "daida", "daidai", "daicho", "daito", "daito", "daido", "taito",
        "daidoji", "daitokuji", "tainaka", "dainari", "dainichi", "tainosho", "tainobu",
        "daihisa", "daifu", "daibu", "daibutsu", "daibo", "daibo", "daihoji", "taima", "daimaruya", "daimo", "taiyo", "taiyoshi", "taira",
        "daira", "tairaku", "dairaku", "tairadate", "dairokuno", "tau", "tauchi", "taenaka", "taera", "taoda",
        "taono", "taohata", "taomura", "taomo", "taomoto", "taka", "taga", "daga", "takaara", "tagai", "takaiso", "takaichi",
        "tagaito", "takaine", "takauji", "takauma", "takaesu", "takaenoki", "takao", "takaoka", "takaochi",
        "takagaki", "takagasa", "takaki", "takagi", "takaku", "takakusaki", "takakusu", "takakuta", "takakura", "takakuwa",
        "takane", "takazakura", "takashi", "takatsukasa", "takashige", "takashita", "takajikko", "takashina", "takashima",
        "takashimizu", "takasho", "tagashira", "takasu", "takasuga", "takasugi", "takasugo", "takasuna", "takase",
        "takaso", "takasode", "takata", "tagata", "takadate", "takatama", "takachi",
    )

    def kana_name(self):
        '''
        @example 'アオタ アキラ'
        '''
        pattern = self.random_element(self.kana_formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_kana_name(cls):
        '''
        @example 'アキラ'
        '''
        return cls.random_element(cls.first_kana_names)

    @classmethod
    def first_kana_name_female(cls):
        return cls.random_element(cls.first_kana_names_female)

    @classmethod
    def first_kana_name_male(cls):
        return cls.random_element(cls.first_kana_names_male)

    @classmethod
    def last_kana_name(cls):
        '''
        @example 'アオタ'
        '''
        return cls.random_element(cls.last_kana_names)

    def romanized_name(self):
        '''
        @example 'Akira Aota'
        '''
        pattern = self.random_element(self.romanized_formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_romanized_name(cls):
        '''
        @example 'Akira'
        '''
        return cls.random_element(cls.first_romanized_names)

    @classmethod
    def first_romanized_name_female(cls):
        return cls.random_element(cls.first_romanized_names_female)

    @classmethod
    def first_romanized_name_male(cls):
        return cls.random_element(cls.first_romanized_names_male)

    @classmethod
    def last_romanized_name(cls):
        '''
        @example 'Aota'
        '''
        return cls.random_element(cls.last_romanized_names)

