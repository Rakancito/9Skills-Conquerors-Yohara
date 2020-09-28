#Search in CPythonPlayer::CPythonPlayer(void)

m_ppyGameWindow = NULL;

#add before

#ifdef ENABLE_CONQUEROR_LEVEL
	m_kMap_dwAffectIndexToSkillIndex.insert(make_pair(int(CInstanceBase::AFFECT_CHEONUN), 182));
#endif