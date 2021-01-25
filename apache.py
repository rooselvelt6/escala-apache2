# Autor: Rooselvelt Angulo

class Apache():
	""" 
		Acute Physiology And Cronic Health Evaluation II

		(Indice de gravedad Apache II):

		Se trata de un sistema de valoración pronostica de mortalidad,  
		que  consiste  en  detectar  los  trastornos fisiológicos  agudos  que  
		atentan  contra  la  vida  del paciente  y  se fundamenta  en  la  
		determinación  de  las  alteraciones de  variables  fisiológicas  
		y  de  parámetros  de  laboratorio,  cuya puntuación es un factor 
		predictivo de mortalidad.

		Objetivos: 

			 Clasificar a los pacientes de acuerdo a la escala Apache II

			• Determinar la condición de egreso de los pacientes

			• Clasificar a los pacientes en sobrevivientes y no
			sobrevivientes

			• Determinar la prevalencia de principales diagnósticos de ingreso

			• Cuantificar la frecuencia de ingreso de acuerdo a la edad
			• Cuantificar la frecuencia de ingreso de acuerdo al sexo

			• Determinar la frecuencia de ingreso de acuerdo al	servicio de procedencia

			• Establecer los días de estancia promedio basado en machine learning
			

		Pacientes: todos los pacientes ingresados a la UCI

		Año de creación: 1985

		Variables fisiológicas: 12

		Puntuación:
			A: APS ACUTE PHYSIOLOGY SCORE: SUMA 12 VARIABLES


	"""
	def __init__(self):

		self.nombre = "APACHE II"

		self.puntaje_total = 0

		self.funciones_medidas = []
		
		self.apache = 0

	# Puntuación A: Sumatoria de todas las Variables fisiológicas

	def temperatura(self, valor_medido, puntaje=0, rango="", nombre="temperatura"):
		""" Función que calcula la temperatura """

		if(valor_medido <= 29.9 ):
			puntaje += 4
			rango = "bajo"

		elif(valor_medido >= 30.0 and valor_medido <= 31.9):
			puntaje += 3
			rango = "bajo"

		elif(valor_medido >= 32.0 and valor_medido <= 33.9):
			puntaje += 2
			rango = "bajo"

		elif(valor_medido >= 34.0 and valor_medido <= 35.9):
			puntaje += 1
			rango = "bajo"

		elif(valor_medido >= 36.0 and valor_medido <= 38.4):
			puntaje += 0
			rango = "normal"

		elif(valor_medido >= 38.5 and valor_medido <= 38.9):
			puntaje += 1
			rango = "alto"

		elif(valor_medido >= 39.0 and valor_medido <= 40.9):
			puntaje += 3
			rango = "alto"

		elif(valor_medido >= 41.0):
			puntaje += 4
			rango = "alto"
		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
	
	def presion_arterial_media(self, valor_medido, puntaje=0, rango="", nombre="presión arterial media (mmHg)"):
		""" Función que calcula la presión arterial media """

		# Validar ingreso de datos solo númericos con try-except

		if(valor_medido <= 49 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 50 and valor_medido <= 69):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 70 and valor_medido <= 109):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 110 and valor_medido <= 129):
			puntaje = 2
			rango = "alto"

		elif(valor_medido >= 130 and valor_medido <= 159):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 160):
			puntaje = 4
			rango = "alto"
		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
		
	def frecuencia_cardiaca(self, valor_medido, puntaje=0, rango="", nombre="frecuencia cardiaca (respuesta ventricular)"):
		""" Función que calcula la frecuencia cardiaca """

		# Validar ingreso de datos solo númericos con try-except

		if(valor_medido <= 39 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 40 and valor_medido <= 54):
			puntaje = 3
			rango = "bajo"

		elif(valor_medido >= 55 and valor_medido <= 69):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 70 and valor_medido <= 109):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 110 and valor_medido <= 139):
			puntaje = 2
			rango = "alto"

		elif(valor_medido >= 140 and valor_medido <= 179):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 180):
			puntaje = 4
			rango = "alto"

		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
		
	def frecuencia_respiratoria(self, valor_medido, puntaje=0, rango="", nombre="frecuencia respiratoria (no ventilado o ventilado)"):
		""" Función que calcula la frecuencia respiratoria """

		if(valor_medido <= 5 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 6 and valor_medido <= 9):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 10 and valor_medido <= 11):
			puntaje = 1
			rango = "bajo"

		elif(valor_medido >= 12 and valor_medido <= 24):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 25 and valor_medido <= 34):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 35 and valor_medido <= 49):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 50):
			puntaje = 4
			rango = "alto"
		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada

	def oxigenacion(self, valor_medido, FiO2=0.5, puntaje=0, rango="", nombre="oxigenación"):
		if(FiO2 >= 0.5):
			anotar = "P AaDO2"
			if(valor_medido < 200):
				puntaje = 0
				rango = "normal"

			elif(valor_medido >= 200 and valor_medido <= 349):
				puntaje = 2
				rango = "alto"

			elif(valor_medido >= 350 and valor_medido <= 499):
				puntaje = 3
				rango = "alto"

			elif(valor_medido >= 500):
				puntaje = 4
				rango = "alto"

		elif(FiO2 < 0.5):
			anotar = "PaO2"
			if(valor_medido > 70):
				puntaje = 0
				rango = "normal"

			elif(valor_medido >= 61 and valor_medido <= 70):
				puntaje = 1
				rango = "bajo"

			elif(valor_medido >= 55 and valor_medido <= 60):
				puntaje = 3
				rango = "bajo"

			elif(valor_medido < 55):
				puntaje = 4
				rango = "bajo"
			
		else:
			print("Valor incorrecto")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango, anotar, FiO2))   # Registrar la función en la lista en caso de ser calculada 

	def pH_arterial(self, valor_medido, puntaje=0, rango="", nombre="pH arterial (Preferido)"):
		""" Función que calcula el Ph Arterial """

		# Validar ingreso de datos solo númericos con try-except

		if(valor_medido <= 7.15 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 7.15 and valor_medido <= 7.24):
			puntaje = 3
			rango = "bajo"

		elif(valor_medido >= 7.25 and valor_medido <= 7.32):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 7.33 and valor_medido <= 7.49):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 7.50 and valor_medido <= 7.59):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 7.60 and valor_medido <= 7.69):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 7.70):
			puntaje = 4
			rango = "alto"
		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
	
	def hco3_serico(self, valor_medido, puntaje=0, rango="", nombre="HCO3 sérico (venoso mEq/L)"):
		""" Función que calcula HCO3 sérico """

		if(valor_medido < 15.0):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 15.0 and valor_medido <= 17.9):
			puntaje = 3
			rango = "bajo"

		elif(valor_medido >= 18.0 and valor_medido <= 21.9):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 22.0 and valor_medido <= 31.9):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 32.0 and valor_medido <= 40.9):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 41.0 and valor_medido <= 51.9):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 52.0):
			puntaje = 4
			rango = "alto"

		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))  # Registrar la función en la lista en caso de ser calculada
	
	def sodio_serico(self, valor_medido, puntaje=0, rango="", nombre="Sodio sérico (mEq/L)"):
		""" Función que calcula la temperatura """

		# Validar ingreso de datos solo númericos con try-except

		if(valor_medido <= 110 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 111 and valor_medido <= 119):
			puntaje = 3
			rango = "bajo"

		elif(valor_medido >= 120 and valor_medido <= 129):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 130 and valor_medido <= 149):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 150 and valor_medido <= 154):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 155 and valor_medido <= 159):
			puntaje = 2
			rango = "alto"

		elif(valor_medido >= 160 and valor_medido <= 179):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 180):
			puntaje = 4
			rango = "alto"

		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
	
	def potasio_serico(self, valor_medido, puntaje=0, rango="", nombre="Potasio sérico (mEq/L)"):
		""" Función que calcula la temperatura """

		# Validar ingreso de datos solo númericos con try-except

		if(valor_medido < 2.5 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 2.5 and valor_medido <= 2.9):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 3.0 and valor_medido <= 3.4):
			puntaje = 1
			rango = "bajo"

		elif(valor_medido >= 3.5 and valor_medido <= 5.4):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 5.5 and valor_medido <= 5.9):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 6.0 and valor_medido <= 6.9):
			puntaje = 3
			rango = "alto"

		elif(valor_medido >= 7.0):
			puntaje = 4
			rango = "alto"
		else:
			print("Valor medido fuera del rango !!!")
		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
		
	def creatinina_serico(self, valor_medido, puntaje=0, rango="", nombre="Creatinina sérico (mg/dL)",  falla_renal=False):
		""" Función que calcula la creatinina serica el valor es doble en caso de falla renal """

		if(falla_renal==False):

			if(valor_medido < 0.6 ):
				puntaje = 2
				rango = "bajo"

			elif(valor_medido >= 0.6 and valor_medido <= 1.4):
				puntaje = 0
				rango = "normal"

			elif(valor_medido >= 1.5 and valor_medido <= 1.9):
				puntaje = 2
				rango = "alto"

			elif(valor_medido >= 2.0 and valor_medido <= 3.4):
				puntaje = 3
				rango = "alto"

			elif(valor_medido >= 3.5):
				puntaje = 4
				rango = "alto"
			else:
				print("Valor medido fuera del rango !!!")
		else:

			if(valor_medido < 0.6 ):
				puntaje = 4
				rango = "bajo"

			elif(valor_medido >= 0.6 and valor_medido <= 1.4):
				puntaje = 0
				rango = "normal"

			elif(valor_medido >= 1.5 and valor_medido <= 1.9):
				puntaje = 4
				rango = "alto"

			elif(valor_medido >= 2.0 and valor_medido <= 3.4):
				puntaje = 6
				rango = "alto"

			elif(valor_medido >= 3.5):
				puntaje = 8
				rango = "alto"

			else:
				print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango, falla_renal))   # Registrar la función en la lista en caso de ser calculada
	
	def hematocrito(self, valor_medido, puntaje=0, rango="", nombre="Hematócrito (%)"):
		""" Función que calcula el hematócrito """

		if(valor_medido < 20.0 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 20.0 and valor_medido <= 29.9):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 30.0 and valor_medido <= 45.9):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 46.0 and valor_medido <= 49.9):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 50.0 and valor_medido <= 59.9):
			puntaje = 2
			rango = "alto"

		elif(valor_medido >= 60.0):
			puntaje = 4
			rango = "alto"

		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, valor_medido, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
	
	def leucocitos(self, valor_medido, puntaje=0, rango="", nombre="Leucocitos (Total/mm3 en miles)"):
		""" Función que calcula los leucocitos """

		if(valor_medido < 1.0 ):
			puntaje = 4
			rango = "bajo"

		elif(valor_medido >= 1.0 and valor_medido <= 2.9):
			puntaje = 2
			rango = "bajo"

		elif(valor_medido >= 3.0 and valor_medido <= 14.9):
			puntaje = 0
			rango = "normal"

		elif(valor_medido >= 15.0 and valor_medido <= 19.9):
			puntaje = 1
			rango = "alto"

		elif(valor_medido >= 20.0 and valor_medido <= 39.9):
			puntaje = 2
			rango = "alto"

		elif(valor_medido >= 40.0):
			puntaje = 4
			rango = "alto"

		else:
			print("Valor medido fuera del rango !!!")

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 
		self.funciones_medidas.append((nombre, puntaje, rango))   # Registrar la función en la lista en caso de ser calculada
	
	def escala_glasgow(self, puntajes=0, nombre="Escala de Glasgow"):

		def apertura_ocular():

			print("*******************************************")
			print("      APERTURA OCULAR DEL PACIENTE         ")
			print("*******************************************")
			print("(1) Espontánea                             ")
			print("(2) A la orden                             ")
			print("(3) Ante un estimulo doloroso              ")
			print("(4) Ausencia de apertura ocular            ")
			print("*******************************************")
			opcion = int(input("Opcion:"))

			if(opcion == 1):
				puntaje = 4

			elif(opcion == 2):
				puntaje = 3

			elif(opcion == 3):
				puntaje = 2

			elif(opcion == 4):
				puntaje = 1

			else:
				print("Opción invalida")

			return puntaje

		def respuesta_verbal():

			print("*******************************************")
			print("     RESPUESTA VERBAL DEL PACIENTE         ")
			print("*******************************************")
			print("(1) Orientado correctamente                ")
			print("(2) Paciente confuso                       ")
			print("(3) Lenguaje inapropiado                   ")
			print("(4) Lenguaje incomprensible                ")
			print("(5) Carencia de actividad verbal           ")
			print("*******************************************")
			opcion = int(input("Opcion:"))

			if(opcion == 1):
				puntaje = 5

			elif(opcion == 2):
				puntaje = 4

			elif(opcion == 3):
				puntaje = 3

			elif(opcion == 4):
				puntaje = 2

			elif(opcion == 5):
				puntaje = 1

			else:
				print("Opción invalida")
				
			return puntaje

		def respuesta_motora():

			print("****************************************************")
			print("         RESPUESTA MOTORA DEL PACIENTE              ")
			print("****************************************************")
			print("(1) Obedece ordenes correctamente                   ")
			print("(2) Localiza estimulos dolorosos                    ")
			print("(3) Responde al estímulo doloroso pero no localiza  ")
			print("(4) Respuesta con flexión anormal de los miembros   ")
			print("(5) Respuesta con extensión anormal de los miembros ")
			print("(6) Ausencia de respuesta motora                    ")
			print("****************************************************")
			opcion = int(input("Opcion:"))

			if(opcion == 1):
				puntaje = 6

			elif(opcion == 2):
				puntaje = 5

			elif(opcion == 3):
				puntaje = 4

			elif(opcion == 4):
				puntaje = 3

			elif(opcion == 5):
				puntaje = 2

			elif(opcion == 6):
				puntaje = 1

			else:
				print("Opción invalida")
				
			return puntaje

		a = apertura_ocular()
		b = respuesta_verbal()
		c = respuesta_motora()

		puntaje = a + b + c

		self.puntaje_total += puntaje # Incrementar el puntaje total del sistema 

		self.funciones_medidas.append((nombre, puntaje))   # Registrar la función en la lista en caso de ser calculada
		
	# Fin de la Puntuación A

	# Puntuación B: Edad
	def edad(self, valor_medido, nombre="Edad"):

		if(valor_medido < 44):
			puntaje = 0

		elif(valor_medido >= 45 and valor_medido <= 54):
			puntaje = 2

		elif(valor_medido >= 55 and valor_medido <= 64):
			puntaje = 3

		elif(valor_medido >= 65 and valor_medido <= 74):
			puntaje = 5

		elif(valor_medido >= 75):
			puntaje = 6

		else:
			print("Valor medido fuera de rango")

		self.apache += puntaje # Incrementar el puntaje total del sistema 
		#self.funciones_medidas.append((nombre, valor_medido, puntaje))   # Registrar la función en la lista en caso de ser calculada
	# Fin de la puntuación B

	# Puntaje C
	def enfermedad_cronica(self):
		""" o. Si existe inmunocompromiso, insuficiencia hepática cardiaca, renal o
			respiratoria y es sometido a un procedimiento quirúrgico programado deberán sumarse 2 puntos al
			total, pero si es sometido a un procedimiento de urgencias, deberán sumarse 5 puntos
		"""
		print("**********************************************")
		print("(1) Paciente con Postcirugía o no quirúrgico *")
		print("(2) Postcirugía electiva                     *")
		print("**********************************************")
		opcion = int(input("Ingrese estado del paciente:"))
		if(opcion==1):
			self.apache += 5
		elif(opcion==2):
			self.apache += 2
		else:
			raise
	
	# Fin del Puntaje C

	def prediccion_mortalidad(self, quirurgico=False):

		if(quirurgico==True):
			if(self.puntaje_total >= 0 and self.puntaje_total <= 4):
				self.mortalidad = 2

			elif(self.puntaje_total >= 5 and self.puntaje_total <= 9):
				self.mortalidad = 4

			elif(self.puntaje_total >= 10 and self.puntaje_total <= 14):
				self.mortalidad = 8

			elif(self.puntaje_total >= 15 and self.puntaje_total <= 19):
				self.mortalidad = 12

			elif(self.puntaje_total >= 20 and self.puntaje_total <= 24):
				self.mortalidad = 29

			elif(self.puntaje_total >= 25 and self.puntaje_total <= 29):
				self.mortalidad = 35

			elif(self.puntaje_total >= 30 and self.puntaje_total <= 34):
				self.mortalidad = 70

			elif(self.puntaje_total > 34):
				self.mortalidad = 88
			else:
				self.mortalidad = 0
		else:

			if(self.puntaje_total >= 0 and self.puntaje_total <= 4):
				self.mortalidad = 4

			elif(self.puntaje_total >= 5 and self.puntaje_total <= 9):
				self.mortalidad = 8

			elif(self.puntaje_total >= 10 and self.puntaje_total <= 14):
				self.mortalidad = 12

			elif(self.puntaje_total >= 15 and self.puntaje_total <= 19):
				self.mortalidad = 25

			elif(self.puntaje_total >= 20 and self.puntaje_total <= 24):
				self.mortalidad = 40

			elif(self.puntaje_total >= 25 and self.puntaje_total <= 29):
				self.mortalidad = 50

			elif(self.puntaje_total >= 30 and self.puntaje_total <= 34):
				self.mortalidad = 70

			elif(self.puntaje_total > 34):
				self.mortalidad = 80

	def variables_fisiologicas_usadas(self):
		""" Sumatoria de las 12 variables fisiologicas """
		return len(self.funciones_medidas)

	def calcular_aps(self):
		""" Calcular la sumatoria de las 12 variables fisiologicas opcional """
		for punto in (self.funciones_medidas):
			self.puntaje_total += punto[2]

	def get_aps(self):
		return self.puntaje_total

	def get_apache(self):
		return self.apache + self.get_aps()

	def get_indicadores(self):
		import pprint
		print("APS:", self.get_aps())
		print("APACHE II:", self.get_apache())
		print("Cantidad de variables fisiológicas:",self.variables_fisiologicas_usadas())
		print("Mediciones realizadas al paciente:")
		pprint.pprint(self.funciones_medidas)
			

	

