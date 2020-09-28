//Search

};

const int aiItemMagicAttributePercentHigh[ITEM_ATTRIBUTE_MAX_LEVEL] =
{
	
//add before
#ifdef ENABLE_CONQUEROR_LEVEL
	{ POINT_INVINCIBLE, },
#endif

	
//Search
    { NULL,		0			}
};
// from import_item_proto.c

//add before
#ifdef ENABLE_CONQUEROR_LEVEL
	{ "INVINCIBLE", APPLY_INVINCIBLE },
#endif

