//Search

bool CHARACTER::Damage(LPCHARACTER pAttacker, int dam, EDamageType type) 
{
	
//add after
#ifdef ENABLE_CONQUEROR_LEVEL	
	if(IsAffectFlag(AFF_CHUNWOON_MOOJUK))
	{
		SendDamagePacket(pAttacker, 0, DAMAGE_BLOCK);
		return false;
	}
#endif	

//Search
				case SKILL_HWAJO:
					{
						int iUseArrow = 1;
						if (iUseArrow == m_me->GetArrowAndBow(&pkBow, &pkArrow, iUseArrow))
						{
							m_me->OnMove(true);
							pkVictim->OnMove();

							if (pkVictim->CanBeginFight())
								pkVictim->BeginFight(m_me);

							sys_log(0, "%s hwajo %s", m_me->GetName(), pkVictim->GetName());
							m_me->ComputeSkill(m_bType, pkVictim);
							m_me->UseArrow(pkArrow, iUseArrow);
						}
					}

					break;
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
				case SKILL_PUNGLOEPO:
					{
						int iUseArrow = 1;
						if (iUseArrow == m_me->GetArrowAndBow(&pkBow, &pkArrow, iUseArrow))
						{
							m_me->OnMove(true);
							pkVictim->OnMove();

							if (pkVictim->CanBeginFight())
								pkVictim->BeginFight(m_me);

							sys_log(0, "%s pungloepo %s", m_me->GetName(), pkVictim->GetName());
							m_me->ComputeSkill(m_bType, pkVictim);
							m_me->UseArrow(pkArrow, iUseArrow);
						}
					}

					break;
#endif
//Search
				case SKILL_PABEOB:
//add after
#ifdef ENABLE_CONQUEROR_LEVEL
				case SKILL_ILGWANGPYO:
				case SKILL_MABEOBAGGWI:
				case SKILL_METEO:
#endif
