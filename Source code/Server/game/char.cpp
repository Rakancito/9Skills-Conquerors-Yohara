//Search in void CHARACTER::Initialize()

	m_pkChrTarget = NULL;

// add after

#ifdef ENABLE_CONQUEROR_LEVEL
	m_pkCheonunEvent = NULL;
#endif

// Search
	StopMuyeongEvent();
	
// add after
#ifdef ENABLE_CONQUEROR_LEVEL
	StopCheonunEvent();
#endif

