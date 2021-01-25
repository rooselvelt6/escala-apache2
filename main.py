# Autor: Rooselvelt Angulo
 
import apache

def main():
	simulador = apache.Apache() # Instancia Apache 2
	print("***********************")
	print("Sistema Apache Terminal")
	print("***********************")

	# Solicitar datos al usuario para el calculo de las funciones fisiologicas
	
	# Puntaje A:
	temperatura = simulador.temperatura(29.9) # Temperatura 
	pam = simulador.presion_arterial_media(49) # Presión arterial media
	fc = simulador.frecuencia_cardiaca(39)
	fr = simulador.frecuencia_respiratoria(5)
	oxigeno = simulador.oxigenacion(500, 0.5)
	hco3 = simulador.hco3_serico(15.0)
	sodio = simulador.sodio_serico(110)
	potasio = simulador.potasio_serico(2.4)
	creatinina = simulador.creatinina_serico(3.5, falla_renal=True)
	hematocrito = simulador.hematocrito(19)
	leucocitos = simulador.leucocitos(0.5)
	glasgow = simulador.escala_glasgow(7)
	
	# Puntaje B:
	simulador.edad(78)

	# Puntaje C:
	simulador.enfermedad_cronica()

	# Indicadores:
	
	simulador.get_indicadores()
   
if __name__ == '__main__':
	main()