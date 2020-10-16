//Search in bool CPythonPlayer::__CanAttack()

if (pkInstMain->IsMountingHorse() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 20))

//Replace with

#ifdef ENABLE_CONQUEROR_LEVEL
	if (pkInstMain->IsMountingHorse() && pkInstMain->IsNewMount() && (GetSkillGrade(107) < 1 && GetSkillLevel(107) < 11))
#else
	if (pkInstMain->IsMountingHorse() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 20))
#endif
