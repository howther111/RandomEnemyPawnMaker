#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.messagebox
import time
import json
import random
import CreateMachineNumber
import CreatePetName
import CreatePilotName
import create_weapon_al
import tkinter.ttk as ttk

### <チェックボタン生成用の関数を事前定義>
### <チェックボタン生成用の関数を事前定義>
def createMultiCheckButton(baseFrame, nameList, checkBoxes, checkBoxVars):
    for i, name in enumerate(nameList):
        checkBoxVars.append(tkinter.BooleanVar())
        checkBoxVars[i].set(False)  # 初期値を明示的にcheckにしておく
        checkBoxes.append(tkinter.Checkbutton(baseFrame, text=name, variable=checkBoxVars[i]))
        checkBoxes[i].pack(anchor=tkinter.W,pady=10)
    root.update()   # 描画の更新
    baseFrame.configure(height=checkBoxes[i].winfo_y()+checkBoxes[i].winfo_height()+20)   # baseFrameの大きさ調整　winfo_height()+20 : pady=20 equivalent

class GuardianData():
    size_list = ["S", "M", "M", "M", "L"]
    special_list = ["トール", "オーディン", "フツノミタマ", "タケミカヅチ"
        , "ヘイムダル", "エーギル", "バルドル", "ヘル", "ニョルド", "ネルガル"
        , "ミューズ", "スィン", "ティール", "ヘルモード", "マリーシ"]
    character_name = ""
    guardian_name = ""
    guardian_type = ""
    guardian_type_list = ["モブ", "ソロ", "強敵"]
    guardian_class = ""
    guardian_class_list = ["奈落獣", "艦船", "ミーレス（マシンザウルス）", "アビスミーレス（マシンザウルス）",
                           "ガーディアン（マシンザウルス）", "アビスガーディアン（マシンザウルス）",
                           "ミーレス（カバリエ）", "アビスミーレス（カバリエ）",
                           "ガーディアン（カバリエ）", "アビスガーディアン（カバリエ）", "ドラゴン", "奈落の使徒"]
    level = 0
    guardian_size = ""
    player_name = ""
    strong_total = 0
    strong_bonus = 0
    reflex_total = 0
    reflex_bonus = 0
    sense_total = 0
    sense_bonus = 0
    intellect_total = 0
    intellect_bonus = 0
    will_total = 0
    will_bonus = 0
    bllesing_total = 0
    bllesing_bonus = 0
    add_fortune_point = 0
    outfits_total_hit = 0
    outfits_total_dodge = 0
    outfits_total_magic = 0
    outfits_total_countermagic = 0
    outfits_total_action = 0
    outfits_total_fp = 0
    outfits_total_hp = 0
    outfits_total_mp = 0
    outfits_total_attack = 0
    outfits_total_battlespeed_total = 0

    outfits_rightname = ""
    outfits_rightattack = ""
    outfits_rightrange = ""
    outfits_rightstrong = "なし"
    outfits_righttarget = ""

    outfits_leftname = ""
    outfits_leftattack = ""
    outfits_leftrange = ""
    outfits_leftstrong = "なし"
    outfits_lefttarget = ""

    outfits_magicrightname = ""
    outfits_magicrightattack = ""
    outfits_magicrightrange = ""
    outfits_magicrightstrong = "なし"
    outfits_magicrighttarget = ""

    outfits_magicleftname = ""
    outfits_magicleftattack = ""
    outfits_magicleftrange = ""
    outfits_magicleftstrong = "なし"
    outfits_magiclefttarget = ""

    armourstotal_slash = 0
    armourstotal_pierce = 0
    armourstotal_crash = 0
    armourstotal_fire = 0
    armourstotal_ice = 0
    armourstotal_thunder = 0
    armourstotal_light = 0
    armourstotal_dark = 0

    items = []
    specials = []

    break_flg = 0

    url = ""

    def input_data(self, level=5, guardian_type="ソロ", guardian_class="ミーレス（カバリエ）",
                   weapon_var=["白兵", "射撃", "魔導"], short_weapon_num="1", long_weapon_num="1"):
        self.guardian_type = guardian_type
        self.guardian_class = guardian_class
        self.url = "https://elaunomitsugi.booth.pm/items/7242399"

        if "モンスター" in guardian_class:
            self.character_name = "奈落獣" + CreatePilotName.CreatePilotName()
            self.guardian_name = self.character_name
        elif "ドラゴン" in guardian_class:
            self.character_name = CreatePilotName.CreatePilotName() + "ドラゴン"
            self.guardian_name = self.character_name
        elif "ソルジャー" in guardian_class:
            self.character_name = CreatePilotName.CreatePilotName() + "・" + CreatePilotName.CreatePilotName()
            self.guardian_name = self.character_name
        elif "ロボット" in guardian_class:
            self.character_name = CreateMachineNumber.CreateMachineNumber() + " " + CreatePetName.CreatePetName()
            self.guardian_name = self.character_name
        elif guardian_class == "艦船":
            ship_list = ["駆逐艦", "巡洋艦", "軽巡洋艦", "重巡洋艦", "戦艦", "空母", "強襲揚陸艦"]
            self.character_name = CreatePilotName.CreatePilotName() + "・" + CreatePilotName.CreatePilotName()
            self.guardian_name = ship_list[random.randint(0, len(ship_list) - 1)] + CreatePetName.CreatePetName()
        elif guardian_class == "ミーレス（マシンザウルス）" or guardian_class == "ガーディアン（マシンザウルス）" or guardian_class == "アビスミーレス（マシンザウルス）"or guardian_class == "アビスガーディアン（マシンザウルス）":
            self.character_name = CreatePilotName.CreatePilotName() + "・" + CreatePilotName.CreatePilotName()
            self.guardian_name = "機械恐竜" + CreatePilotName.CreatePilotName()
        else:
            self.character_name = CreatePilotName.CreatePilotName() + "・" + CreatePilotName.CreatePilotName()
            self.guardian_name = CreateMachineNumber.CreateMachineNumber() + " " + CreatePetName.CreatePetName()

        self.guardian_type = guardian_type
        self.level = level
        self.guardian_size = self.size_list[random.randint(0, len(self.size_list) - 1)]
        if guardian_class == "艦船":
            self.guardian_size = "XL"

        self.player_name = "エネミー"
        self.strong_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.strong_bonus = int(self.strong_total / 3)
        self.reflex_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.reflex_bonus = int(self.reflex_total / 3)
        self.sense_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.sense_bonus = int(self.sense_total / 3)
        self.intellect_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.intellect_bonus = int(self.intellect_total / 3)
        self.will_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.will_bonus = int(self.will_total / 3)
        self.bllesing_total = 3 + max(0, random.randint(0,6) + random.randint(0, self.level))
        self.bllesing_bonus = int(self.bllesing_total / 3)

        special_num = 0
        if "シャード" in guardian_class:
            special_num = 3
        elif "アビス" in guardian_class:
            special_num = max(3, (random.randint(0, self.level) * 2) - random.randint(0, self.level))

        if special_num > 0:
            self.specials.append(self.special_list[random.randint(0, len(self.special_list) - 1)])

            for i in range(special_num - 1):
                try:
                    specialnum = i + 1
                    specialstr = "specials." + str(specialnum).zfill(3) + ".name"
                    self.specials.append(self.special_list[random.randint(0, len(self.special_list) - 1)])
                except:
                    pass

        self.outfits_total_hit = 7 + max(0, (random.randint(0, self.level) * 2) - random.randint(0, self.level))
        self.outfits_total_dodge = 1 + max(0, (random.randint(0, self.level) * 2) - random.randint(0, self.level))
        self.outfits_total_magic = 7 + max(0, (random.randint(0, self.level) * 2) - random.randint(0, self.level))
        self.outfits_total_countermagic = 1 + max(0,
                                                  (random.randint(0, self.level) * 2) - random.randint(0, self.level))
        self.outfits_total_action = 4 + max(0, (random.randint(0, self.level) * 2) - random.randint(0, self.level))
        if self.guardian_type == "モブ":
            self.outfits_total_fp = max(10,
                                        (random.randint(self.level - 2, self.level) * 10) + (random.randint(1, 10) * 1))
        elif self.guardian_type == "ソロ":
            self.outfits_total_fp = max(5,
                                        (random.randint(self.level - 2, self.level) * 7) + (random.randint(1, 7) * 1))
        elif self.guardian_type == "強敵":
            self.outfits_total_fp = max(50,
                                        (random.randint(self.level - 2, self.level) * 20) + (random.randint(1, 20) * 1))
        self.outfits_total_hp = max(10, (random.randint(self.level - 2, self.level) * 5) + (random.randint(1, 5) * 1))
        self.outfits_total_mp = max(10, (random.randint(self.level - 2, self.level) * 5) + (random.randint(1, 5) * 1))
        self.outfits_total_battlespeed_total = self.outfits_total_action + 5
        #self.outfits_total_battlespeed_total = self.outfits_total_battlespeed_total.replace("ﾏｽ", "")

        self.add_fortune_point = 0

        main_weapon_short_flg = False
        sub_weapon_short_flg = False
        main_weapon_long_flg = False
        sub_weapon_long_flg = False
        short_weapon_num_int = int(short_weapon_num)
        long_weapon_num_int = int(long_weapon_num)
        short_got_weapon_num = 0
        long_got_weapon_num = 0
        print(weapon_var)
        maxloop = 1000
        loop = 0

        while (short_got_weapon_num < short_weapon_num_int or long_got_weapon_num < long_weapon_num_int) and loop < maxloop:
            print("max_short_weapon_num = " + str(short_weapon_num_int))
            print("max_long_weapon_num = " + str(long_weapon_num_int))
            print("short_weapon_num = " + str(short_got_weapon_num))
            print("long_weapon_num = " + str(long_got_weapon_num))
            weapon = create_weapon_al.create_weapon(self.level)
            weapon_weapon_type = weapon.weapon_type
            if short_got_weapon_num < short_weapon_num_int and "白兵" in weapon_var and weapon_weapon_type == "白兵" and main_weapon_short_flg == False:
                self.outfits_rightname = weapon.weapon_name
                self.outfits_rightattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_rightrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_righttarget = weapon.target
                short_got_weapon_num = short_got_weapon_num + 1
                main_weapon_short_flg = True
                print("白兵")

            elif short_got_weapon_num < short_weapon_num_int and "白兵" in weapon_var and weapon_weapon_type == "白兵" and main_weapon_short_flg == True and sub_weapon_short_flg == False:
                self.outfits_leftname = weapon.weapon_name
                self.outfits_leftattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_leftrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_lefttarget = weapon.target
                short_got_weapon_num = short_got_weapon_num + 1
                sub_weapon_short_flg = True
                print("白兵")

            elif short_got_weapon_num < short_weapon_num_int and "射撃" in weapon_var and weapon_weapon_type == "射撃" and main_weapon_short_flg == False:
                self.outfits_rightname = weapon.weapon_name
                self.outfits_rightattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_rightrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_righttarget = weapon.target
                short_got_weapon_num = short_got_weapon_num + 1
                main_weapon_short_flg = True
                print("射撃")

            elif short_got_weapon_num < short_weapon_num_int and "射撃" in weapon_var and weapon_weapon_type == "射撃" and main_weapon_short_flg == True and sub_weapon_short_flg == False:
                self.outfits_leftname = weapon.weapon_name
                self.outfits_leftattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_leftrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_lefttarget = weapon.target
                short_got_weapon_num = short_got_weapon_num + 1
                sub_weapon_short_flg = True
                print("射撃")

            elif long_got_weapon_num < long_weapon_num_int and "魔導" in weapon_var and weapon_weapon_type == "魔導" and main_weapon_long_flg == False:
                self.outfits_magicrightname = weapon.weapon_name
                self.outfits_magicrightattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_magicrightrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_magicrighttarget = weapon.target
                long_got_weapon_num = long_got_weapon_num + 1
                main_weapon_long_flg = True
                print("魔導")

            elif long_got_weapon_num < long_weapon_num_int and "魔導" in weapon_var and weapon_weapon_type == "魔導" and main_weapon_long_flg == True and sub_weapon_long_flg == False:
                self.outfits_magicleftname = weapon.weapon_name
                self.outfits_magicleftattack = weapon.element + "+" + str(weapon.attack)
                self.outfits_magicleftrange = str(weapon.min_range) + "-" + str(weapon.max_range)
                self.outfits_magiclefttarget = weapon.target
                long_got_weapon_num = long_got_weapon_num + 1
                sub_weapon_long_flg = True
                print("魔導")

            loop = loop + 1


        self.armourstotal_slash = random.randint(0, self.level)
        self.armourstotal_pierce = random.randint(0, self.level)
        self.armourstotal_crash = random.randint(0, self.level)
        self.armourstotal_fire = random.randint(0, self.level)
        self.armourstotal_ice = random.randint(0, self.level)
        self.armourstotal_thunder = random.randint(0, self.level)
        self.armourstotal_light = random.randint(0, self.level)
        self.armourstotal_dark = random.randint(0, self.level)

        print(self.guardian_name)
        
    def output_prompt_guardian(self, image_type="モンスター"):
        text = "文字を描くことなく、以下の特徴を持つ" + image_type + "の全身像を描いてください。 " + \
        "背景：白 カラーリング：自由 " + \
        "右腕武装：" + self.outfits_rightname + " " + \
        "左腕武装：" + self.outfits_leftname + " " + \
        "右肩武装：" + self.outfits_magicrightname + " " + \
        "左肩武装：" + self.outfits_magicleftname
        file_name = self.guardian_name + "_エネミープロンプトデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("エネミープロンプトデータを生成しました")

    def output_text(self):
        # 駒のテキストデータを出力する
        text = self.guardian_name + "\n" + \
                   "PL:" + self.player_name + "\n" + \
                   "レベル:" + str(self.level) + \
                   " サイズ:" + self.guardian_size + "\n"\
                   "分類:" + self.guardian_type + \
                   " クラス:" + self.guardian_class

        #text = text + "\n財産ポイント:" + self.add_fortune_point

        text = text + "\n【命中】" + str(self.outfits_total_hit) + \
                   "【回避】" + str(self.outfits_total_dodge) + \
                   "【魔導】" + str(self.outfits_total_magic) + \
                   "【抗魔】" + str(self.outfits_total_countermagic) + \
                   "【行動】" + str(self.outfits_total_action) + \
                   "\n【HP】" + str(self.outfits_total_fp) + \
                   "【MP】" + str(self.outfits_total_mp) + \
                   "【移動力】" + str(self.outfits_total_battlespeed_total) + "m"

        text = text + "\n加護:"
        if (len(self.specials) == 0):
            text = text + "なし" + "/"
        for special in self.specials:
            text = text + special + "/"
        text = text[:-1]

        outfits_rightrangem = ""
        if self.outfits_rightrange != "":
            outfits_rightrangem = str(int(self.outfits_rightrange[-1:]) * 5) + "m"
            if outfits_rightrangem == "0m":
                outfits_rightrangem = "至近"

        outfits_leftrangem = ""
        if self.outfits_leftrange != "":
            outfits_leftrangem = str(int(self.outfits_leftrange[-1:]) * 5) + "m"
            if outfits_leftrangem == "0m":
                outfits_leftrangem = "至近"

        outfits_righttargetm = self.outfits_righttarget
        if self.outfits_righttarget == "単体":
            pass
        else:
            outfits_righttargetm = "範囲（選択）"

        outfits_lefttargetm = self.outfits_lefttarget
        if self.outfits_lefttarget == "単体":
            pass
        else:
            outfits_lefttargetm = "範囲（選択）"

        outfits_magicrighttargetm = self.outfits_magicrighttarget
        if self.outfits_magicrighttarget == "単体":
            pass
        else:
            outfits_magicrighttargetm = "範囲（選択）"

        outfits_magiclefttargetm = self.outfits_magiclefttarget
        if self.outfits_magiclefttarget == "単体":
            pass
        else:
            outfits_magiclefttargetm = "範囲（選択）"

        outfits_magicrightrangem = ""
        if self.outfits_magicrightrange != "":
            outfits_magicrightrangem = str(int(self.outfits_magicrightrange[-1:]) * 5) + "m"
            if outfits_magicrightrangem == "0m":
                outfits_magicrightrangem = "至近"

        outfits_magicleftrangem = ""
        if self.outfits_magicleftrange != "":
            outfits_magicleftrangem = str(int(self.outfits_magicleftrange[-1:]) * 5) + "m"
            if outfits_magicleftrangem == "0m":
                outfits_magicleftrangem = "至近"

        if not self.outfits_rightname == "":
            text = text + "\n[*]主近:" + self.outfits_rightname + \
                   " 射程:" + outfits_rightrangem + \
                   " 代償:" + self.outfits_rightstrong + \
                   "\n攻撃力:" + self.outfits_rightattack + \
                   " 対象:" + outfits_righttargetm

        if not self.outfits_leftname == "":
            text = text + "\n[*]副近:" + self.outfits_leftname + \
                   " 射程:" + outfits_leftrangem + \
                   " 代償:" + self.outfits_leftstrong + \
                   "\n攻撃力:" + self.outfits_leftattack + \
                   " 対象:" + outfits_lefttargetm

        if not self.outfits_magicrightname == "":
            text = text + "\n[*]主遠:" + self.outfits_magicrightname + \
                   " 射程:" + outfits_magicrightrangem + \
                   " 代償:" + self.outfits_magicrightstrong + \
                   "\n攻撃力:" + self.outfits_magicrightattack + \
                   " 対象:" + outfits_magicrighttargetm

        if not self.outfits_magicleftname == "":
            text = text + "\n[*]副遠:" + self.outfits_magicleftname + \
                   " 射程:" + outfits_magicleftrangem + \
                   " 代償:" + self.outfits_magicleftstrong + \
                   "\n攻撃力:" + self.outfits_magicleftattack + \
                   " 対象:" + outfits_magiclefttargetm

        text = text + "\n防御力:斬" + str(self.armourstotal_slash) + \
                "/刺" + str(self.armourstotal_pierce) + \
                "/殴" + str(self.armourstotal_crash) + \
                "/炎" + str(self.armourstotal_fire) + \
                "/氷" + str(self.armourstotal_ice) + \
                "/雷" + str(self.armourstotal_thunder) + \
                "/光" + str(self.armourstotal_light) + \
                "/闇" + str(self.armourstotal_dark)

        print(text)

        file_name = self.guardian_name + "_エネミーテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("エネミーテキストデータを生成しました")
        self.output_pawn(text)

    def output_online_json_data(self):
        self.outfits_rightattack_array = self.outfits_rightattack.split("+")
        self.outfits_leftattack_array = self.outfits_leftattack.split("+")
        self.outfits_magicrightattack_array = self.outfits_magicrightattack.split("+")
        self.outfits_magicleftattack_array = self.outfits_magicleftattack.split("+")

        jsontext = {}
        jsontext["data"] = {}
        jsontext["data"]["guardian_name"] = self.guardian_name
        jsontext["data"]["character_name"] = self.character_name
        jsontext["data"]["player_name"] = self.player_name
        jsontext["data"]["level"] = max(0, int(self.level))
        jsontext["data"]["size"] = self.guardian_size
        jsontext["data"]["hit"] = max(0, int(self.outfits_total_hit))
        jsontext["data"]["dodge"] = max(0, int(self.outfits_total_dodge))
        jsontext["data"]["magic"] = max(0, int(self.outfits_total_magic))
        jsontext["data"]["countermagic"] = max(0, int(self.outfits_total_countermagic))
        jsontext["data"]["action"] = max(0, int(self.outfits_total_action))
        jsontext["data"]["fp"] = max(0, int(self.outfits_total_fp))
        jsontext["data"]["hp"] = max(0, int(self.outfits_total_hp))
        jsontext["data"]["mp"] = max(0, int(self.outfits_total_mp))
        jsontext["data"]["battlespeed"] = max(0, int(self.outfits_total_battlespeed_total))
        jsontext["data"]["mws_name"] = self.outfits_rightname

        if self.outfits_rightrange == "":
            jsontext["data"]["mws_shortrange"] = 0
            jsontext["data"]["mws_longrange"] = 0
        else:
            jsontext["data"]["mws_shortrange"] = int(self.outfits_rightrange[:1])
            jsontext["data"]["mws_longrange"] = int(self.outfits_rightrange[-1:])

        jsontext["data"]["mws_attack"] = max(0, int(self.outfits_rightattack_array[1]))
        jsontext["data"]["mws_element"] = self.outfits_rightattack_array[0]
        jsontext["data"]["sws_name"] = self.outfits_leftname

        if self.outfits_leftrange == "":
            jsontext["data"]["sws_shortrange"] = 0
            jsontext["data"]["sws_longrange"] = 0
        else:
            jsontext["data"]["sws_shortrange"] = int(self.outfits_leftrange[:1])
            jsontext["data"]["sws_longrange"] = int(self.outfits_leftrange[-1:])

        jsontext["data"]["sws_attack"] = max(0, int(self.outfits_leftattack_array[1]))
        jsontext["data"]["sws_element"] = self.outfits_leftattack_array[0]
        jsontext["data"]["mwl_name"] = self.outfits_magicrightname

        if self.outfits_magicrightrange == "":
            jsontext["data"]["mwl_shortrange"] = 0
            jsontext["data"]["mwl_longrange"] = 0
        else:
            jsontext["data"]["mwl_shortrange"] = int(self.outfits_magicrightrange[:1])
            jsontext["data"]["mwl_longrange"] = int(self.outfits_magicrightrange[-1:])

        jsontext["data"]["mwl_attack"] = max(0, int(self.outfits_magicrightattack_array[1]))
        jsontext["data"]["mwl_element"] = self.outfits_magicrightattack_array[0]
        jsontext["data"]["swl_name"] = self.outfits_magicleftname

        if self.outfits_magicleftrange == "":
            jsontext["data"]["swl_shortrange"] = 0
            jsontext["data"]["swl_longrange"] = 0
        else:
            jsontext["data"]["swl_shortrange"] = int(self.outfits_magicleftrange[:1])
            jsontext["data"]["swl_longrange"] = int(self.outfits_magicleftrange[-1:])

        jsontext["data"]["swl_attack"] = max(0, int(self.outfits_magicleftattack_array[1]))
        jsontext["data"]["swl_element"] = self.outfits_magicleftattack_array[0]
        jsontext["data"]["armourstotal_slash"] = max(0, int(self.armourstotal_slash))
        jsontext["data"]["armourstotal_pierce"] = max(0, int(self.armourstotal_pierce))
        jsontext["data"]["armourstotal_crash"] = max(0, int(self.armourstotal_crash))
        jsontext["data"]["armourstotal_fire"] = max(0, int(self.armourstotal_fire))
        jsontext["data"]["armourstotal_ice"] = max(0, int(self.armourstotal_ice))
        jsontext["data"]["armourstotal_thunder"] = max(0, int(self.armourstotal_thunder))
        jsontext["data"]["armourstotal_light"] = max(0, int(self.armourstotal_light))
        jsontext["data"]["armourstotal_dark"] = max(0, int(self.armourstotal_dark))
        jsontext["data"]["cost"] = (jsontext["data"]["hit"] * 100)
        jsontext["data"]["cost"] = (jsontext["data"]["dodge"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["magic"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["countermagic"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["action"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["fp"] * 10) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["hp"] * 10) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["mp"] * 10) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["battlespeed"] * 200) +  jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["mws_longrange"])) * 200) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["mws_shortrange"])) * -100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["mws_attack"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["sws_longrange"])) * 200) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["sws_shortrange"])) * -100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["sws_attack"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["mwl_longrange"])) * 200) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["mwl_shortrange"])) * -100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["mwl_attack"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["swl_longrange"])) * 200) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (min(10, max(0, jsontext["data"]["swl_shortrange"])) * -100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["swl_attack"] * 100) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_slash"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_pierce"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_crash"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_fire"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_ice"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_thunder"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_light"] * 50) + jsontext["data"]["cost"]
        jsontext["data"]["cost"] = (jsontext["data"]["armourstotal_dark"] * 50) + jsontext["data"]["cost"]

        # 出力
        file_name = self.guardian_name + "_エネミーオンラインデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(json.dumps(jsontext, indent=4, ensure_ascii=False))
        f.close()

        print("エネミーオンラインデータを生成しました")

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.guardian_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.outfits_total_action)
        jsontext["data"]["status"] = []

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][0]["label"] = "HP"
        jsontext["data"]["status"][0]["value"] = self.outfits_total_fp
        jsontext["data"]["status"][0]["max"] = self.outfits_total_fp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][1]["label"] = "MP"
        jsontext["data"]["status"][1]["value"] = self.outfits_total_mp
        jsontext["data"]["status"][1]["max"] = self.outfits_total_mp

        '''

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][2]["label"] = "財産ポイント"
        jsontext["data"]["status"][2]["value"] = self.add_fortune_point
        jsontext["data"]["status"][2]["max"] = self.add_fortune_point

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][3]["label"] = "ブレイク"
        jsontext["data"]["status"][3]["value"] = 1
        jsontext["data"]["status"][3]["max"] = 1
        
        '''

        i = 2

        for special in self.specials:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = special
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        for item in self.items:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = item
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        jsontext["data"]["params"] = []

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "体力基本値"
        jsontext["data"]["params"][0]["value"] = str(self.strong_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "反射基本値"
        jsontext["data"]["params"][1]["value"] = str(self.sense_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "知覚基本値"
        jsontext["data"]["params"][2]["value"] = str(self.strong_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "理知基本値"
        jsontext["data"]["params"][3]["value"] = str(self.intellect_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "意志基本値"
        jsontext["data"]["params"][4]["value"] = str(self.will_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "幸運基本値"
        jsontext["data"]["params"][5]["value"] = str(self.bllesing_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][6]["label"] = "体力B"
        jsontext["data"]["params"][6]["value"] = str(self.strong_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][7]["label"] = "反射B"
        jsontext["data"]["params"][7]["value"] = str(self.sense_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][8]["label"] = "知覚B"
        jsontext["data"]["params"][8]["value"] = str(self.strong_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][9]["label"] = "理知B"
        jsontext["data"]["params"][9]["value"] = str(self.intellect_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][10]["label"] = "意志B"
        jsontext["data"]["params"][10]["value"] = str(self.will_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][11]["label"] = "幸運B"
        jsontext["data"]["params"][11]["value"] = str(self.bllesing_bonus)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][12]["label"] = "命中値"
        jsontext["data"]["params"][12]["value"] = str(self.outfits_total_hit)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][13]["label"] = "回避値"
        jsontext["data"]["params"][13]["value"] = str(self.outfits_total_dodge)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][14]["label"] = "魔導値"
        jsontext["data"]["params"][14]["value"] = str(self.outfits_total_magic)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][15]["label"] = "抗魔値"
        jsontext["data"]["params"][15]["value"] = str(self.outfits_total_countermagic)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][16]["label"] = "行動値"
        jsontext["data"]["params"][16]["value"] = str(self.outfits_total_action)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][17]["label"] = "移動力"
        jsontext["data"]["params"][17]["value"] = str(self.outfits_total_battlespeed_total)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][18]["label"] = "斬防御"
        jsontext["data"]["params"][18]["value"] = str(self.armourstotal_slash)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][19]["label"] = "刺防御"
        jsontext["data"]["params"][19]["value"] = str(self.armourstotal_pierce)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][20]["label"] = "殴防御"
        jsontext["data"]["params"][20]["value"] = str(self.armourstotal_crash)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][21]["label"] = "炎防御"
        jsontext["data"]["params"][21]["value"] = str(self.armourstotal_fire)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][22]["label"] = "氷防御"
        jsontext["data"]["params"][22]["value"] = str(self.armourstotal_ice)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][23]["label"] = "雷防御"
        jsontext["data"]["params"][23]["value"] = str(self.armourstotal_thunder)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][24]["label"] = "光防御"
        jsontext["data"]["params"][24]["value"] = str(self.armourstotal_light)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][25]["label"] = "闇防御"
        jsontext["data"]["params"][25]["value"] = str(self.armourstotal_dark)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][26]["label"] = "状態"
        jsontext["data"]["params"][26]["value"] = "通常"

        outfits_rightattack_array = self.outfits_rightattack.split("+")
        outfits_leftattack_array = self.outfits_leftattack.split("+")
        outfits_magicrightattack_array = self.outfits_magicrightattack.split("+")
        outfits_magicleftattack_array = self.outfits_magicleftattack.split("+")

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        commandtext = "//アクション\nムーブ:\nマイナー:\nメジャー:\n//リソース\n" + \
                                       "C({HP}-YY)　残りHP\n" + \
                                       "C({EN}-YY)　残りEN\n\n" + \
                                       "//防御、+0欄に修正を記入\nAL+{回避値}+0　近・回避\n" \
                                       "AL+{抗魔値}+0　遠・抗魔\nC(XX-{}-0)　被ダメージ、{}内に防御属性3文字\n\n" \
                                       "//攻撃、+0欄に修正を記入\nAL+{命中値}+0　近・命中\nAL+{魔導値}+0　遠・魔導\n"

        if self.outfits_rightname != "":
            commandtext = commandtext + "2d6+" + outfits_rightattack_array[1] + "+0　" + \
                                       "〈" + outfits_rightattack_array[0] + "〉" + \
                                       self.outfits_rightname + "ダメージ\n"

        if self.outfits_leftname != "":
            commandtext = commandtext + "2d6+" + outfits_leftattack_array[1] + "+0　" + \
                                       "〈" + outfits_leftattack_array[0] + "〉" + \
                                       self.outfits_leftname + "ダメージ\n"

        if self.outfits_magicrightname != "":
                commandtext = commandtext + "2d6+" + outfits_magicrightattack_array[1] + "+0　" + \
                                       "〈" + outfits_magicrightattack_array[0] + "〉" + \
                                       self.outfits_magicrightname + "ダメージ\n"

        if self.outfits_magicleftname != "":
                commandtext = commandtext + "2d6+" + outfits_magicleftattack_array[1] + "+0　" + \
                                       "〈" + outfits_magicleftattack_array[0] + "〉" + \
                                       self.outfits_magicleftname + "ダメージ\n"

        commandtext = commandtext + "\n//能力値判定\nAL+{体力B}  体力判定\nAL+{反射B}  反射判定\nAL+{知覚B}  " \
                                       "知覚判定\nAL+{理知B}  理知判定\nAL+{意志B}  意志判定\nAL+{幸運B}  幸運判定"


        jsontext["data"]["commands"] = commandtext
        jsontext["data"]["externalUrl"] = self.url
        file_name = self.guardian_name + "_エネミー駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("エネミー駒データを生成しました")


def get_data(level=3, guardian_type="ソロ", guardian_class="モンスター", weapon_var=[],
             short_weapon_num="1", long_weapon_num="1"):
    weapon_var_list = []
    for checkbox in weapon_var:
        weapon_var_list.append(checkbox.get())

    weapon_var_list2 = []
    if weapon_var_list[0] == True:
        weapon_var_list2.append("白兵")
    if weapon_var_list[1] == True:
        weapon_var_list2.append("射撃")
    if weapon_var_list[2] == True:
        weapon_var_list2.append("魔導")

    guardian = GuardianData()
    time.sleep(5)

    print(weapon_var)
    print("short_weapon_number = " + str(short_weapon_num))
    print("long_weapon_number = " + str(long_weapon_num))
    print(weapon_var_list2)

    guardian.input_data(level=level, guardian_type=guardian_type, guardian_class=guardian_class,
                        weapon_var=weapon_var_list2, short_weapon_num=short_weapon_num, long_weapon_num=long_weapon_num)
    guardian.output_text()
    if "モンスター" in guardian_class:
        guardian.output_prompt_guardian(image_type="モンスター")
    elif "ドラゴン" in guardian_class:
        guardian.output_prompt_guardian(image_type="ドラゴン")
    elif "ソルジャー" in guardian_class:
        guardian.output_prompt_guardian(image_type="人物")
    elif "ロボット" in guardian_class:
        guardian.output_prompt_guardian(image_type="ロボット")
    elif guardian_class == "艦船":
        guardian.output_prompt_guardian(image_type="宇宙戦艦")
    else:
        guardian.output_prompt_guardian(image_type="モンスター")

    #guardian.output_online_json_data()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"アルシャードセイヴァーRPG ココフォリア用エネミーデータ作成ツール")
    root.geometry("400x450")

    frame1 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame2 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame3 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame4 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame5 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame6 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame7 = tkinter.Frame(root, width=200, height=150)  # Button, Entry
    frame8 = tkinter.Frame(root, width=200, height=150)  # Button, Entry
    frame9 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame10 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame11 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame12 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame13 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame14 = tkinter.Frame(root, width=200, height=50)  # Button, Entry

    frame1.propagate(False)
    frame2.propagate(False)
    frame3.propagate(False)
    frame4.propagate(False)
    frame5.propagate(False)
    frame6.propagate(False)
    frame7.propagate(False)
    frame8.propagate(False)
    frame9.propagate(False)
    frame10.propagate(False)
    frame11.propagate(False)
    frame12.propagate(False)
    frame13.propagate(False)
    frame14.propagate(False)

    # Frameを配置（grid）
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=1, column=0)
    frame4.grid(row=1, column=1)
    frame5.grid(row=2, column=0)
    frame6.grid(row=2, column=1)
    frame7.grid(row=3, column=0)
    frame8.grid(row=3, column=1)
    frame9.grid(row=4, column=0)
    frame10.grid(row=4, column=1)
    frame11.grid(row=5, column=0)
    frame12.grid(row=5, column=1)
    frame13.grid(row=6, column=0)
    frame14.grid(row=6, column=1)

    # ラベル
    Static1 = tkinter.Label(frame1, text=u'レベル')
    Static1.pack()

    # エントリー
    EditBox = tkinter.Entry(frame2, width=25)
    EditBox.pack()

    # ラベル
    Static2 = tkinter.Label(frame3, text=u'分類')
    Static2.pack()

    # エントリー
    ComboBox1 = ttk.Combobox(frame4, width=25, values=["モブ", "ソロ", "強敵"])
    ComboBox1.pack()

    # ラベル
    Static3 = tkinter.Label(frame5, text=u'クラス')
    Static3.pack()

    # エントリー
    ComboBox2 = ttk.Combobox(frame6, width=25, values=["モンスター", "シャードモンスター",
                                                       "アビスモンスター", "艦船", "ソルジャー",
                                                       "シャードソルジャー", "アビスソルジャー",
                                                       "ロボット", "シャードロボット",
                                                       "アビスロボット", "ドラゴン", "シャードドラゴン", "アビスドラゴン"])
    ComboBox2.pack()

    # ラベル
    Static4 = tkinter.Label(frame7, text=u'武装の種類')
    Static4.pack()

    # 値保持用の配列を定義
    checkBoxes = []
    checkBoxVars = []

    nameList = ["白兵", "射撃", "魔導"]
    # checkBox作成関数を呼び出して描画
    createMultiCheckButton(frame8, nameList, checkBoxes, checkBoxVars)

    for checkbox in checkBoxes:
        checkbox.select()

    # ラベル
    Static5 = tkinter.Label(frame9, text=u'近接武装の数')
    Static5.pack()

    shortrnd = random.randint(0, 2)
    longrnd = random.randint(0, 2)
    if shortrnd == 0 and longrnd == 0:
        shortrnd = 1
        longrnd = 1

    # エントリー
    ComboBox3 = ttk.Combobox(frame10, width=25, values=["0", "1",
                                                       "2"])
    ComboBox3.current(str(shortrnd))
    ComboBox3.pack()

    # ラベル
    Static6 = tkinter.Label(frame11, text=u'遠隔武装の数')
    Static6.pack()

    # エントリー
    ComboBox4 = ttk.Combobox(frame12, width=25, values=["0", "1",
                                                        "2"])
    ComboBox4.current(str(longrnd))
    ComboBox4.pack()

    Button1 = tkinter.Button(frame13, text=u'生成', command=lambda: [get_data(int(EditBox.get()), ComboBox1.get(), ComboBox2.get(), checkBoxVars, ComboBox3.get(), ComboBox4.get())])
    Button1.pack()

    # ボタン
    Button2 = tkinter.Button(frame14, text=u'終了', command=lambda: root.quit())
    Button2.pack()

    root.mainloop()