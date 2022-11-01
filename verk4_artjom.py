# Artjom Pushkar | 2506063540

import random

loop = True
while loop:
    print("\nBókstafir/tölustafir [1]")
    print("Strengur [2]")
    print("Strengjarugl [3]")
    print("Klipping [4]")
    print("Hástafir / lágstafir / tölustafir [5]")
    print("Kennitala [6]")
    print("Stafahrap [7]")
    print("Hætta [99]")
    val = input("\nVeldu lið: ")
    
    
    #lidur 1
    #Skrifaðu forrit sem tekur inn textastreng ( inn í textastreng geta verið tölustafir ). 
    #Forritið á síðan að finna fjölda bókstafa og fjölda tölustafa og prenta viðeigandi texta um það á skjáinn.
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Lína 25, það hvetur til textainntaks frá notandanum, athugar síðan hvort bókstafir og tölustafir séu til staðar (lína 27 til 33), 
    #ef þeir eru til, þá er þeim bætt við einn af öðrum við dalk, ef bæði tölustafi og bókstafi vantar birtist villa, sem segir um það, í línum (35 - 36) 
    #er prentuð á skjánum og þegar fyrir neðan eins og venjulega er skipun sem spyr um mögulega endurtekningu þessa liðs
    
    if val == "1":
        on = True
        while on:
            str = input("\nSkrifaðu texta: ")
            digit=letter=0
            for ch in str:
                if ch.isdigit(): # efð það eru bókstafir
                    digit=digit+1 # fer þessi lina i gang (sem checkar fjölda stafa)
                elif ch.isalpha(): # her er verið að checka um tölustafi
                    letter=letter+1 # sama og i linu 32
                else:
                    print("Villa! Engin texti var sleginn eða symbol er ekki til")
                    
            print("Fjöldi bókstafa: ", letter)
            print("Fjöldi tölustafa: ", digit)
            
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
     
     
    #lidur 2
    #Skrifaðu forrit sem tekur inn textastreng. Forritið athugar síðan hvort strengurinn er samhverfur þ.e.a.s. að strengurinn sé eins aftur á bak og áfram. 
    #Dæmi um samhverfa strengi eru amma og abba. Forritið á ekki að vera stafnæmt sem þýðir að strengurinn Abba er samhverfur þó að fyrsti stafur sé stórt 'A' og síðasti lítið 'a'.
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Í þessu verki, upphaflega, eins og í fyrri málsgrein, er beðið um orð, í þessu tilfelli um speglun þess, ef orðið er enn mögulegt að snúa við samsvarandi textastreng birtist (68 - 69) 
    # ef hið gagnstæða gerist að ekki er hægt að spegla orðið, birtist textinn einnig um þessa línu (65 - 66) 
            
    elif val == "2":
        on = True
        while on:
            word = input("\nSláðu inn texta: ").lower() # input
            word2 = word[::-1] # Flippar texta
            
            if word != word2: # efð firsta orðið og flippað orð eru ekki eins fer lina 67 i gang
                print(word ," er ekki samhverfur strengur")
                
            elif word == word2: # ef orðin eru eins, fer lina 70 i gang
                print(word, " er samhverfur strengur")
                
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
        
                
    #lidur 3            
    #Skrifaðu forrit sem tekur inn tvö orð og býr til nýtt orð sem er búið til af tveim fyrstu og tveim síðustu stöfum orðanna. Passa þarf að orðin séu að minnsta kosti 5 stafa löng hvort. Látið notandann slá inn annað orð ef orðin ná ekki 5 stöfum hvort.
    #Síðan á forritið að gera eftirfarandi og prenta viðeigandi texta um það á skjáinn.
    #• Nýja samsetta orðið
    #• Nýja samsetta orðið í hástöfum
    #• Finna heildarlengd nýja orðsins         
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Það er beðið um tvö orð, síðan í línum (97 - 98) er lengd þeirra mæld, þá athugar hugtakið (101) lengd þeirra, ef þau eru fleiri en 5 eða jafnt og 5 stöfum, 
    # þá gengur kóðinn lengra, annars kóðinn byrjar aftur, lína (102 - 102) klippir fyrstu 2 stafina úr báðum orðum strengsins (105 - 106) 
    # snýr orðunum við, með sömu reglu klippum við út tvo stafi úr báðum orðum aðeins gagnstæða strenginn (108 - 109) 
    # flettu þeim síðan aftur á strenginn (111 - 112) eftir að við límdum alla stafi línuna (114) fyrir neðan gefum þeim færibreytur, til dæmis litla / stóra stafi, þá prentum við þá bara
               
    elif val == "3":
        on = True
        while on:
            word1 = input("\nSláðu inn fyrsta orð: ")
            word2 = input("Sláðu inn annað orð: ")
            
            word3 = len(word1)# faum lengd orða
            word4 = len(word2)# faum lengd orða
            
            
            if word3 and word4 >= 5:
                ord1 = word1[:2] #tekur 2 stafi
                ord2 = word2[:2] #tekur 2 stafi
                
                word5 = word1[::-1] #flippar orðum
                word6 = word2[::-1] #flippar orðum
                
                ord3 = word5[:2] #tekur 2 stafi
                ord4 = word6[:2] #tekur 2 stafi
                
                ord3 = ord3[::-1] #flippar stöfum aftur
                ord4 = ord4[::-1] #flippar stöfum aftur
                
                ord5 = ord1 + ord2 + ord3 + ord4 # limum stafina saman
                
                ord6 = ord5.lower()
                ord7 = ord5.upper()
                
                ord8 = len(ord5)
                print("Nýji strengurinn er: ", ord6)
                print("Nýji strengurinn í upphafsstöfum: ", ord7)
                print("Nýji strengurinn í lágstöfum: ", ord6)
                print("Lengd strengjanna er " , ord8 , " stafir")
                
            elif word3 or word4 < 5:
                print("\nVeldu önnur orð")
            
            else: 
                print("\nVilla með inslátt")
                
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
        
    
    #lidur 4
    #Skrifaðu forrit þar sem beðið er um nafn. Forritið tekur sneið úr nafninu, fyrst allt nafnið, síðan allt nema fyrsta bókstafinn o.s.fvr. og skrifar á skjáinn. 
    #Forritið skal leyst með lykkju. Úttak forrits ætti að vera líkt og hér fyrir neðan:    
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Hér er allt frekar einfalt, við biðjum um notendanafn og eftir það tökum við bara og fjarlægjum fyrsta stafinn, með því að nota for lykkju
            
    elif val == "4":
        on = True
        while on:
            name = input("\nSkrifaðu nafn: ")     
            lengd1 = len(name) #faum lengd nafns
            
            for len in range(len(name)): # for lykkja sem fer i gegnum nafnið td. Artjom - 6 stafir
                print(name[len:]) # prentir út nafnið alltaf án stafs (lykt - dæmi += dæmi)
                
                
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
             
                
    #lidur 5          
    #Skrifaðu forrit sem tekur inn textastreng ( inn í textastreng geta verið tölustafir ). Forritið á
    #síðan að breyta hástöfum í lágstafi og lágstöfum í hástafi. Ef tölustafur kemur fyrir í 
    #strengnum er honum breytt í undirstrik ( _ ) eða '#'.
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Við biðjum notandann líka um orð og síðan í línum (187 til 195) athugum við hvort stórir/smáir stafir séu til staðar og einnig tölustafir, 
    # línan (188 - 189) athugar hvort stórir stafir séu til staðar, ef þeir eru, breytast þeir í litlar á línunni ( 189) þá það sama í línunni (192 - 193) aðeins hið gagnstæða, 
    # þeir. er breytt úr litlum í stórt, þá eru strengir (194 - 195) athugaðu fyrir tölustafi, ef svo er þá er þeim skipt út fyrir _ með því að nota streng (185) 
    # það er stafur í strengnum (195) replace er notað til að skipta út tölum með a staf, síðan prentað á skjá        
    
    elif val == "5":
        on = True
        while on:
            word3 = ""
            word = input("\nSkrifaði texta: ")
            symbol1 = "_"
            
            for word2 in word:
                if word2.isupper(): #Faum að vita hvort er til stórir stafir
                    word2 = word2.lower() # ef þau eru til, þá breytast þau i litla stafi
                    
                elif word2.islower(): # sama og ofar, nema öfugt (ur hástöfum i lagstafi)
                    word2 = word2.upper()
                    
                elif word2.isdigit(): # sama nema faum að vita hvort eru til stafir
                        word2 =  word2.replace(word2, symbol1)
                word3 += word2 # faum alla for lykkju i word3
                
            print(word3)
            
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
            
            
    #lidur 6 
    #Skrifaðu forrit sem athugar hvort innslegin kennitala er rétt. Eftirfarandi reglur gilda um rétta 
    #kennitölu: 
    #Lengd 10 stafir. 
    #Mánuður er á bilinu 1-12.
    #Ártölin 0 – 21 merkir þessa öld – Ártölin 22 - 99 merkja öldina sem var að líða. 
    #Mánuðirnir hafa ýmist 28, 30 eða 31 dag.
    #Aukastig ef þú hefur hlaupár með þar sem mánuður 2 er þá með 29 daga. 
    
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Þessi kóði er nokkuð langur, en aðgerðareglu hans er endurtekin 12 sinnum, í upphafi er beðið um kennitölu notandans, 
    # eftir það í línum (237 til 242) er hann skorinn í dag / mánuð / ár og hann úthlutar einnig int tjáningu , en eftir það er talningin reiknuð út. 
    # tölustafir í kennistrengnum (244), ef lengd hans er 10 stafir, þá heldur kóðinn áfram vinnustrengnum sínum (245) eftir það er ártalið athugað, ef allt er rétt, 
    # heldur kóðinn áfram vinnu, síðan er mánuðurinn athugaður, ef það er það sama er rétt er athugað hvort hann fari ekki yfir dagafjölda í ákveðnum mánuði, 
    # eftir það kemur samsvarandi texti upp ef kennitalan passar upp, annars kemur ítrekuð beiðni um kennitöluna með sami textinn             
                          
    elif val == "6":
        on = True 
        while on:
            kt = input("Sláðu inn kennitölu (án bandstriks '-'): ") # input
            
            ktdag = kt[:2] # faum dag
            ktdag = int(ktdag)
            ktman = kt[2:4] # faum mánuð
            ktman = int(ktman)
            ktar = kt[4:6] # faum ár
            ktar = int(ktar)
            
            ktlen = len(kt) # faum lengd kt
            if ktlen == 10: # checkum lengd kt
                if ktar <= 21 or ktar >= 22 or ktar <= 99: # checkum ár
                    if ktman == 1: # ef mánuður er jafn og 1 fer lykkjan fyrir neðan i gang
                        if ktdag <= 31: # her checkar daga
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 2:
                        if ktdag <= 29:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 3:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 4:
                        if ktdag <= 30:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 5:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 6:
                        if ktdag <= 30:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 7:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 8:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 9:
                        if ktdag <= 30:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 10:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 11:
                        if ktdag <= 30:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    elif ktman == 12:
                        if ktdag <= 31:
                            print("Kennitalan er rétt!")
                            svar = input("\nViltu gera aftur? [y/n] ").lower()
                            if svar == 'n':
                                print("Aftur í valmyndina")
                                on = False
                            elif svar == 'y':
                                print("Byrjum upp á nytt")
                            else:
                                print("Vandaðu inslátt")
                        else:
                            print("Kennitalan er vitlaus!")
                    else:
                        print("Mánudur er ekki til, sláðu aftur!")
                else:
                    print("Árið er slegið vitlaust!")
            else:
                print("Villa með inslátt! Reyndu aftur")
             
             
                
    #lidur 7
    #Skrifaðu forrit sem tekur inn textastreng. Klippið svo fremsta stafinn og aftasta stafinn af 
    #orðinu þar til ekkert er eftir eða aðeins einn stafur, við hverja klippingu prentast 
    #textastrengurinn.
    
    #Upplýsingar um hvernig liðurinn var unnin:
    #Forritið biður notandann um hvaða orð sem er, eftir það reiknar það lengd þess í strengnum (423) og síðan, í strengnum (426 til 428), 
    # er það skorið af báðum megin þar til lágmark er eftir, þær. einn karakter
    
    elif val == "7":
        on = True 
        while on:
            word = input("Sláðu inn texta: ")
            lengd = len(word)
            tala = 0
            
            for len in range(lengd, 0,  -1): # for lykkja sem tekur siðasta stafinn
                    print(word[tala:len]) # prentir ut textan
                    tala += 1
                    
            svar = input("\nViltu gera aftur? [y/n] ").lower()
            if svar == 'n':
                print("Aftur í valmyndina")
                on = False
            elif svar == 'y':
                print("Byrjum upp á nytt")
            else:
                print("Vandaðu inslátt")
                    
                         
    elif val == "99":
        print("\nTakk fyrir notkun!")
        loop = False
     
        
    else:
        print("\nVilla með inslátt!")