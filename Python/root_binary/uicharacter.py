#Search

class CharacterWindow(ui.ScriptWindow):
	ACTIVE_PAGE_SLOT_COUNT = 8
	
#Replace with

class CharacterWindow(ui.ScriptWindow):
	if app.ENABLE_CONQUEROR_LEVEL:
		ACTIVE_PAGE_SLOT_COUNT = 9
	else:
		ACTIVE_PAGE_SLOT_COUNT = 8	
		
#Search

	def __init__(self):
	
		self.chDetailsWnd = None
		self.isOpenedDetailsWnd = False
		
		ui.ScriptWindow.__init__(self)
		
		self.state = "STATUS"
		
#add after

		if app.ENABLE_CONQUEROR_LEVEL:
			self.substate = "BASE"
			
		
#Search

	def OnTop(self):
		if self.chDetailsWnd:
			self.chDetailsWnd.SetTop()
			
#add before

		if app.ENABLE_CONQUEROR_LEVEL:
			self.toolTipConquerorInfoButton = None
			
			self.tabSungmaButtonDict = None
			self.SungmaButton = None
			
#Search

	def __BindObject(self):
		self.toolTip = uiToolTip.ToolTip()
		self.toolTipJob = uiToolTip.ToolTip()
		self.toolTipAlignment = uiToolTip.ToolTip(130)	
		
#add after

		if app.ENABLE_CONQUEROR_LEVEL:
			self.toolTipConquerorInfoButton = uiToolTip.ToolTip()
			
			
#Search

		self.skillGroupButton = (
			self.GetChild("Skill_Group_Button_1"),
			self.GetChild("Skill_Group_Button_2"),
		)
		
#add after

		if app.ENABLE_CONQUEROR_LEVEL:
			self.tabSungmaButtonDict = {
				"BASE"		: self.GetChild("change_base_button"),
				"SUNGMA"	: self.GetChild("change_conqueror_button")
			}
			
			self.SungmaPageDict = {
				"BASE" : self.GetChild("base_info"),
				"SUNGMA" : self.GetChild("sungma_info"),
			}
			
			#self.BaseInfoButton = self.GetChild("change_base_button"),
			#self.SungmaInfoButton = self.GetChild("change_conqueror_button")

			#self.BaseInfoButton.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowBaseToolTip)
			#self.BaseInfoButton.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideBaseToolTip)
			
			#self.SungmaInfoButton.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowSungmaToolTip)
			#self.SungmaInfoButton.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideSungmaToolTip)
			
			self.HTH_IMG = self.GetChild("HTH_IMG")
			self.INT_IMG = self.GetChild("INT_IMG")
			self.STR_IMG = self.GetChild("STR_IMG")
			self.DEX_IMG = self.GetChild("DEX_IMG")
			
			self.HTH_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowHTHToolTip)
			self.HTH_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideHTHToolTip)
			
			self.INT_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowINTToolTip)
			self.INT_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideINTToolTip)
			
			self.STR_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowSTRToolTip)
			self.STR_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideSTRToolTip)
			
			self.DEX_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowDEXToolTip)
			self.DEX_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideDEXToolTip)
			
			self.MSPD_IMG = self.GetChild("MSPD_IMG")
			self.ASPD_IMG = self.GetChild("ASPD_IMG")
			self.CSPD_IMG = self.GetChild("CSPD_IMG")
			self.MATT_IMG = self.GetChild("MATT_IMG")
			self.MDEF_IMG = self.GetChild("MDEF_IMG")
			#self.DEX_IMG = self.GetChild("ER_IMG")
			
			self.MSPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowMSPDToolTip)
			self.MSPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideMSPDToolTip)
			
			self.ASPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowASPDToolTip)
			self.ASPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideASPDToolTip)
			
			self.CSPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowCSPDToolTip)
			self.CSPD_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideCSPDToolTip)
			
			self.MATT_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowMATTToolTip)
			self.MATT_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideMATTToolTip)

			self.MDEF_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowMDEFToolTip)
			self.MDEF_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideMDEFToolTip)

			#self.DEX_IMG.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowERToolTip)
			#self.DEX_IMG.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideERToolTip)
			
#Search in def __BindEvent(self):

		for (tabKey, tabButton) in self.tabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabButton), tabKey)
			
#add after

		if app.ENABLE_CONQUEROR_LEVEL:
			for (tabKey, tabButton) in self.tabSungmaButtonDict.items():
				tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabSungmaButton), tabKey)
				
#Search in def __LoadWindow(self):

		self.SetState("STATUS")
		
#add after

		if app.ENABLE_CONQUEROR_LEVEL:
			self.SetSubState("BASE")
			
			
#Search

	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)
		
#add after

	if app.ENABLE_CONQUEROR_LEVEL:
		def __OnClickTabSungmaButton(self, stateKey):
			self.SetSubState(stateKey)
			
			
#Search 

	def GetState(self):
		return self.state
		
#add after

	if app.ENABLE_CONQUEROR_LEVEL:
		def SetSubState(self, stateSubKey):
			
			self.substate = stateSubKey

			for (tabKey, tabButton) in self.tabSungmaButtonDict.items():
				if stateSubKey!=tabKey:
					tabButton.SetUp()

			for pageValue in self.SungmaPageDict.itervalues():
				pageValue.Hide()

			self.SungmaPageDict[stateSubKey].Show()

#Search
	def __HideAlignmentToolTip(self):
		self.toolTipAlignment.HideToolTip()
		
#add after

	if app.ENABLE_CONQUEROR_LEVEL:
		def __ShowHTHToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_IMG_CON)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideHTHToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()

		def __ShowINTToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_IMG_INT)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideINTToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()

		def __ShowSTRToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_IMG_STR)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideSTRToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
			
		def __ShowDEXToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_IMG_DEX)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideDEXToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()

		###############################################################################
		def __ShowBaseToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_BASE_LEVEL)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideBaseToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
		###
		def __ShowSungmaToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_CONQUEROR_LEVEL)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideSungmaToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()			
		
		###
		
		def __ShowMSPDToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_MOVE_SPEED)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideMSPDToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
		####
		def __ShowASPDToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_ATT_SPEED)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideASPDToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
		###	
		def __ShowCSPDToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_CAST_SPEED)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideCSPDToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
			
		###	
		def __ShowMATTToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_MAG_ATT)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideMATTToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
			
		###	
		def __ShowMDEFToolTip(self):
			self.toolTipConquerorInfoButton.ClearToolTip()
			self.toolTipConquerorInfoButton.AutoAppendTextLine(localeInfo.STAT_TOOLTIP_MAG_DEF)
			self.toolTipConquerorInfoButton.AlignHorizonalCenter()
			
			self.toolTipConquerorInfoButton.ShowToolTip()

		def __HideMDEFToolTip(self):
			self.toolTipConquerorInfoButton.HideToolTip()
		##############################################################################################


