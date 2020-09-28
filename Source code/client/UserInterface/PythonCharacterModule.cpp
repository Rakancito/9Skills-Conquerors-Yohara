#Search
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_MALL",					CInstanceBase::NEW_AFFECT_MALL);
	
#add before

#ifdef ENABLE_CONQUEROR_LEVEL
	PyModule_AddIntConstant(poModule, "AFFECT_CHEONUN", CInstanceBase::AFFECT_CHEONUN);
#endif