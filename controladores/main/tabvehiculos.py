from controladores.main.tabclientes import buscar_cli
from controladores.ventmain import Main


def init_tab(self: Main):
	self.ventMain.btnBusCar.clicked.connect(lambda: buscar_cli(self))
