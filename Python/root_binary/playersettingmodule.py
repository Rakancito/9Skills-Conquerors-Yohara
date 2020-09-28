#Search:

		SKILL_INDEX_DICT = {
			JOB_WARRIOR : { 
				1 : (1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0,), 
				2 : (16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0,), 
				"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
			},
			JOB_ASSASSIN : { 
				1 : (31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
				2 : (46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
				"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
			},
			JOB_SURA : { 
				1 : (61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0,),
				2 : (76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0,),
				"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
			},
			JOB_SHAMAN : { 
				1 : (91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0,),
				2 : (106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0,),
				"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
			},
			JOB_WOLFMAN : {
				1 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
				"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
			}
		}

#Replace with
		if app.ENABLE_CONQUEROR_LEVEL:
			SKILL_INDEX_DICT = {
				JOB_WARRIOR : { 
					1 : (1, 2, 3, 4, 5, 6, 0, 0, 176, 137, 0, 138, 0, 139, 0,), 
					2 : (16, 17, 18, 19, 20, 21, 0, 0, 176, 137, 0, 138, 0, 139, 0,), 
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_ASSASSIN : { 
					1 : (31, 32, 33, 34, 35, 36, 0, 0, 177, 137, 0, 138, 0, 139, 0, 140,), 
					2 : (46, 47, 48, 49, 50, 51, 0, 0, 178, 137, 0, 138, 0, 139, 0, 140,), 
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_SURA : { 
					1 : (61, 62, 63, 64, 65, 66, 0, 0, 179, 137, 0, 138, 0, 139, 0,),
					2 : (76, 77, 78, 79, 80, 81, 0, 0, 180, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_SHAMAN : { 
					1 : (91, 92, 93, 94, 95, 96, 0, 0, 181, 137, 0, 138, 0, 139, 0,),
					2 : (106, 107, 108, 109, 110, 111, 0, 0, 182, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_WOLFMAN : {
					1 : (170, 171, 172, 173, 174, 175, 0, 0, 183, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				}
			}
		else:
			SKILL_INDEX_DICT = {
				JOB_WARRIOR : { 
					1 : (1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0,), 
					2 : (16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0,), 
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_ASSASSIN : { 
					1 : (31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
					2 : (46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_SURA : { 
					1 : (61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0,),
					2 : (76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_SHAMAN : { 
					1 : (91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0,),
					2 : (106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				},
				JOB_WOLFMAN : {
					1 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
					"SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 131,),
				}
			}

#In def __LoadGameEffect(): you will need add after last chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+

	if app.ENABLE_CONQUEROR_LEVEL:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+58, "", "d:/ymir work/pc/shaman/effect/chunwoon_4_target.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+59, "Bip01", "d:/ymir work/pc/shaman/effect/chunwoon_moojuk.mse")
		
	#in my case it's +58 and +59, you will need check what is your magic numbers ;)


#Search in def __LoadGameWarriorEx(race, path):

		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "gihyeol" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "gihyeol" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+9, "finish" + END_STRING + ".msa")
		
#Search
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "noegeom" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "noegeom" + END_STRING + ".msa")
#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+24, "finish" + END_STRING + ".msa")



#Search in def __LoadGameAssassinEx(race, path):

		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "seomjeon" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "seomjeon" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+9, "ilgangpyo" + END_STRING + ".msa")
		
#Search
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "seomgwang" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "seomgwang" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+24, "pungraepo" + END_STRING + ".msa")
		

#Search in def __LoadGameSuraEx(race, path):

		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "pabeop" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+9, "akgi" + END_STRING + ".msa")
		
#Search
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "mahwan" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+24, "akgi_dark" + END_STRING + ".msa")
		

#Search in def __LoadGameShamanEx(race, path):

	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+6,	"gicheon_target.msa")

#add after
	if app.ENABLE_CONQUEROR_LEVEL:
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+9,	"meteo.msa")
	
#Search
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+21,	"jeungryeok_target.msa")

#add after
	if app.ENABLE_CONQUEROR_LEVEL:
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+24,	"chunwoon.msa")
	

#Search
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6,	"gicheon" + END_STRING + ".msa")
	
#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+9, "meteo" + END_STRING + ".msa")
		
#Search
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21,	"jeungryeok" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+24, "chunwoon" + END_STRING + ".msa")
		

#If you have wolfman
#Search in def __LoadGameWolfmanEx(race, path):

		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "blue_possession" + END_STRING + ".msa")

#add after
		if app.ENABLE_CONQUEROR_LEVEL:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+9, "pungwoo" + END_STRING + ".msa")

