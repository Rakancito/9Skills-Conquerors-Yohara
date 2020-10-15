//Search
		void				StopMuyeongEvent();
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
		void				StartCheonunEvent(long lApplyValue);
		void				StopCheonunEvent();
#endif

//Search
		LPEVENT				m_pkMuyeongEvent;
		
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
		LPEVENT				m_pkCheonunEvent;
#endif
