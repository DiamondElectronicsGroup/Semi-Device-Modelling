


class schottky():
	def __init__(self, wf_metal, wf_semi, ideality):
		self.wf_metal = wf_metal
		self.wf_semi = wf_semi
		self.ideality = ideality
		self.v_bi = self.wf_semi - self.wf_metal
		self.eff_v_bi = self.v_bi
	
	def current(self, v_app):
		self.eff_v_bi = self.v_bi+((1/self.ideality)*v_app)