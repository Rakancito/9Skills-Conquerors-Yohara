//Search in bool CHARACTER::LearnSkillByBook(DWORD dwSkillVnum, BYTE bProb)

if (GetSkillMasterType(dwSkillVnum) != SKILL_MASTER)
	
//Before add
	

#ifdef ENABLE_CONQUEROR_LEVEL
#ifdef ENABLE_WOLFMAN_CHARACTER
		if (GetSkillMasterType(dwSkillVnum) != SKILL_MASTER && (dwSkillVnum >= SKILL_FINISH && dwSkillVnum <= SKILL_ILIPUNGU))
#else
		if (GetSkillMasterType(dwSkillVnum) != SKILL_MASTER && (dwSkillVnum >= SKILL_FINISH && dwSkillVnum <= SKILL_CHEONUN))
#endif
		{
			if (GetSkillMasterType(dwSkillVnum) > SKILL_MASTER)
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT(TRANSLATE_LANGUAGE, "ÀÌ ½ºÅ³Àº Ã¥À¸·Î ´õÀÌ»ó ¼ö·ÃÇÒ ¼ö ¾ø½À´Ï´Ù."));
				return false;
			}
		}
		else
#endif

//Search in void CHARACTER::SkillLevelUp(DWORD dwVnum, BYTE bMethod)
			
			if (GetSkillMasterType(pkSk->dwVnum) != SKILL_MASTER)
				return;
// Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
#ifdef ENABLE_WOLFMAN_CHARACTER
			if (GetSkillMasterType(pkSk->dwVnum) != SKILL_MASTER && (pkSk->dwVnum< SKILL_FINISH | pkSk->dwVnum> SKILL_ILIPUNGU))
#else
			if (GetSkillMasterType(pkSk->dwVnum) != SKILL_MASTER && (pkSk->dwVnum< SKILL_FINISH | pkSk->dwVnum> SKILL_CHEONUN))
#endif
#else
			if (GetSkillMasterType(pkSk->dwVnum) != SKILL_MASTER)
#endif
				return;

//add after

//Search
	if (dwVnum == SKILL_CHAIN)
	{
		ResetChainLightningIndex();
		AddChainLightningExcept(pkVictim);
	}
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
	else if (dwVnum == SKILL_METEO)
	{
		ComputeSkill(dwVnum, pkVictim);
	}
#endif

//Search
void CHARACTER::StopMuyeongEvent()
{
	event_cancel(&m_pkMuyeongEvent);
}
//add after
#ifdef ENABLE_CONQUEROR_LEVEL

EVENTINFO(cheonun_event_info)
{
    DynamicCharacterPtr ch;
    long lApplyCheonun;
};

EVENTFUNC(skill_cheonun_event)
{
    cheonun_event_info* info = dynamic_cast<cheonun_event_info*>(event->info);

    if (info == NULL)
    {
        sys_err("skill_cheonun_event> <Factor> Null pointer");
        return 0;
    }

    LPCHARACTER ch = info->ch;
    long lValue = info->lApplyCheonun;

    if (ch == NULL || lValue == NULL)
        return 0;

    if (!ch->IsAffectFlag(AFF_CHEONUN))
    {
        ch->StopCheonunEvent();
        return 0;
    }

    long lPercent = number(1, 100);
    if (lPercent <= lValue)
        ch->AddAffect(2000, POINT_NONE, 0, AFF_CHUNWOON_MOOJUK, lValue, 0, true);

    return PASSES_PER_SEC(12);
}

void CHARACTER::StartCheonunEvent(long lApplyValue)
{
    if (m_pkCheonunEvent)
        return;

    cheonun_event_info* info = AllocEventInfo<cheonun_event_info>();

    info->ch = this;
    info->lApplyCheonun = lApplyValue;

    m_pkCheonunEvent = event_create(skill_cheonun_event, info, PASSES_PER_SEC(1));
}

void CHARACTER::StopCheonunEvent()
{
	event_cancel(&m_pkCheonunEvent);
}
#endif

//Search in bool CHARACTER::IsUsableSkillMotion(DWORD dwMotionIndex) const

#ifdef ENABLE_WOLFMAN_CHARACTER
	const DWORD SKILL_NUM = 176;
#else
	const DWORD SKILL_NUM = 158;
#endif

//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
	const DWORD SKILL_NUM = 184;
#else
#ifdef ENABLE_WOLFMAN_CHARACTER
	const DWORD SKILL_NUM = 176;
#else
	const DWORD SKILL_NUM = 158;
#endif
#endif

//Search

	}; // s_anSkill2JobGroup

	const DWORD MOTION_MAX_NUM 	= 124;
	
//add before

#ifdef ENABLE_CONQUEROR_LEVEL
		0, // job_skill(CONQUEROR SKILL) 176
		0, // job_skill(CONQUEROR SKILL) 177
		0, // job_skill(CONQUEROR SKILL) 178
		0, // job_skill(CONQUEROR SKILL) 179
		0, // job_skill(CONQUEROR SKILL) 180
		0, // job_skill(CONQUEROR SKILL) 181
		0, // job_skill(CONQUEROR SKILL) 182
#ifdef ENABLE_WOLFMAN_CHARACTER
		0, // job_skill(CONQUEROR SKILL) 183
#endif
#endif


//Search
		{   0,		0,			0,			0,			0		}, //  9
		
//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
		{   5,		176,			177,			179,			181,	183		}, //  9
#else
		{   0,		0,			0,			0,			0		}, //  9
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  24
		
//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
		{   4,		176,			178,			180,			182		}, //  24
#else
		{   0,		0,			0,			0,			0		}, //  24
#endif


//Search
		{   0,		0,			0,			0,			0		}, //  34

//Replace with

		// ¿©À¯ºÐ
#ifdef ENABLE_CONQUEROR_LEVEL
		{   5,		176,			177,			179,			181,	183		}, //  34
#else
		{   0,		0,			0,			0,			0		}, //  34
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  49
		
//Replace with
#ifdef ENABLE_CONQUEROR_LEVEL
		{   4,		176,			178,			180,			182		}, //  49
#else
		{   0,		0,			0,			0,			0		}, //  49
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  59
		
//Replace with
#ifdef ENABLE_CONQUEROR_LEVEL
		{   5,		176,			177,			179,			181,	183		}, //  59
#else
		{   0,		0,			0,			0,			0		}, //  59
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  74

//Replace with
#ifdef ENABLE_CONQUEROR_LEVEL
		{   5,		176,			178,			180,			182,	183		}, //  74
#else
		{   0,		0,			0,			0,			0		}, //  74
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  84
		
//Replace with
#ifdef ENABLE_CONQUEROR_LEVEL
		{   5,		176,			177,			179,			181,	183		}, //  84
#else
		{   0,		0,			0,			0,			0		}, //  84
#endif

//Search
		{   0,		0,			0,			0,			0		}, //  99
//Replace with
#ifdef ENABLE_CONQUEROR_LEVEL
		{   4,		176,			178,			180,			182		}, //  99
#else
		{   0,		0,			0,			0,			0		}, //  99
#endif

//Search
const int SKILL_COUNT = 6;
static const DWORD SkillList[JOB_MAX_NUM][SKILL_GROUP_MAX_NUM][SKILL_COUNT] =
{
	{ {	1,	2,	3,	4,	5,	6	}, {	16,	17,	18,	19,	20,	21	} },
	{ {	31,	32,	33,	34,	35,	36	}, {	46,	47,	48,	49,	50,	51	} },
	{ {	61,	62,	63,	64,	65,	66	}, {	76,	77,	78,	79,	80,	81	} },
	{ {	91,	92,	93,	94,	95,	96	}, {	106,	107,	108,	109,	110,	111	} },
#ifdef ENABLE_WOLFMAN_CHARACTER
	{ {	170,	171,	172,	173,	174,	175	}, {	0,	0,	0,	0,	0,	0	} },
#endif
};

//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
const int SKILL_COUNT = 7;
static const DWORD SkillList[JOB_MAX_NUM][SKILL_GROUP_MAX_NUM][SKILL_COUNT] =
{
	{ {	1,	2,	3,	4,	5,	6,	176	}, {	16,	17,	18,	19,	20,	21,	176	} },
	{ {	31,	32,	33,	34,	35,	36,	177	}, {	46,	47,	48,	49,	50,	51,	178	} },
	{ {	61,	62,	63,	64,	65,	66,	179	}, {	76,	77,	78,	79,	80,	81,	180	} },
	{ {	91,	92,	93,	94,	95,	96,	181	}, {	106,	107,	108,	109,	110,	111,	182	} },
#ifdef ENABLE_WOLFMAN_CHARACTER
	{ {	170,	171,	172,	173,	174,	175,	183	}, {	0,	0,	0,	0,	0,	0,	0	} },
#endif
};
#else

const int SKILL_COUNT = 6;
static const DWORD SkillList[JOB_MAX_NUM][SKILL_GROUP_MAX_NUM][SKILL_COUNT] =
{
	{ {	1,	2,	3,	4,	5,	6	}, {	16,	17,	18,	19,	20,	21	} },
	{ {	31,	32,	33,	34,	35,	36	}, {	46,	47,	48,	49,	50,	51	} },
	{ {	61,	62,	63,	64,	65,	66	}, {	76,	77,	78,	79,	80,	81	} },
	{ {	91,	92,	93,	94,	95,	96	}, {	106,	107,	108,	109,	110,	111	} },
#ifdef ENABLE_WOLFMAN_CHARACTER
	{ {	170,	171,	172,	173,	174,	175	}, {	0,	0,	0,	0,	0,	0	} },
#endif

};
#endif

