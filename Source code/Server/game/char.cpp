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

//Search
		default:
			sys_err("CHARACTER::PointChange: %s: unknown point change type %d", GetName(), type);
			return;
			
//add before

#ifdef ENABLE_CONQUEROR_LEVEL
		case POINT_INVINCIBLE:
			SetPoint(type, amount);
			val = GetPoint(type);
			break;
#endif
		
// Search

		default:
			sys_err("Unknown apply type %d name %s", bApplyType, GetName());
			break;
			
// add before
#ifdef ENABLE_CONQUEROR_LEVEL
		case APPLY_INVINCIBLE:
#endif
			PointChange(aApplyInfo[bApplyType].bPointType, iVal);
			break;
