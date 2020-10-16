Search in bool CPythonPlayer::__CanUseSkill()

if (pkInstMain->IsMountingHorse() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 20))

//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
	if (pkInstMain->IsMountingHorse() && (GetSkillGrade(107) < 1 && GetSkillLevel(107) < 20))
#else
	if (pkInstMain->IsMountingHorse() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 20))
#endif
