
//Search
		if (pElements->dwType == SKILL_MUYEONG)
			continue;
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
		if (pElements->dwType == SKILL_CHEONUN)
			continue;
#endif

//Search
	if (pkAff->dwType == SKILL_MUYEONG)
	{
		if (bAdd)
			StartMuyeongEvent();
		else
			StopMuyeongEvent();
	}
	
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
    	if (pkAff->dwType == SKILL_CHEONUN)
    	{
        	if (bAdd)
            		StartCheonunEvent(pkAff->lApplyValue);
        	else
            		StopCheonunEvent();
    	}
#endif

//Search
	RemoveAffect(SKILL_GICHEON);
	
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
	RemoveAffect(SKILL_CHEONUN);
#endif
}

//Search
		case (SKILL_GICHEON):
		
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
		case (SKILL_CHEONUN):
#endif
