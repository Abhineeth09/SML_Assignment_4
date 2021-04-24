def apply_piecewise(x):	
	import tf_encrypted as tfe 
	import numpy as np
	import tensorflow as tf
	from tf_encrypted.keras import activations
	#from tf_encrypted.keras.activations import sigmoid
	#from util import sigmoid
	import sys
	sys.path.append('/Users/abhineethmishra/Documents/CSE_598_SML/assignment_4/tfe/tf_encrypted/protocol/pond/')
	#from pond import sigmoid

	#Convert tf tensor to PondPrivateTensor
	def createPondPrivateTensor(tf_tensor):
		@tfe.local_computation
		def provide_input():
			#return tf.convert_to_tensor([[1,0.4,-0.7,0.2],[0,0,1,1]],dtype=float)
		    return tf_tensor#tf.ones(shape=(5, 10))

		# define inputs 
		x = provide_input(player_name='input-provider-0')
		return x
	#w = provide_input(player_name='input-provider-1')

	#Test variable -- substituted as the function argument
	#x = createPondPrivateTensor(tf.ones(shape=(5, 10)))

	#returns a numpy array from a PondPrivateTensor
	def PPT_to_numpy(tensor):
		return tf.keras.backend.get_value(x.reveal().to_native())


	#Implementing the function in the question
	def piecewise(number):
		#print(number)
		number = float(number)
		if number < -0.5:
			#print(number,'return 0')
			return 0
		elif number >= -0.5 and number < 0.5:
			#print(number,'return ',0.5+float(number))
			return (0.5+float(number))
		elif number>=0.5:
			#print(number,'return 1')
			return 1
	func = np.vectorize(piecewise)
	#print(PPT_to_numpy(x))
	a = func(PPT_to_numpy(x))
	#print(a)
	np_array = PPT_to_numpy(x)
	print(np_array)
	for index, value in np.ndenumerate(np_array):
		np_array[index[0],index[1]] = piecewise(value)
	applied_function_tensor = tf.convert_to_tensor(np_array)
	print(np_array,createPondPrivateTensor(applied_function_tensor))
	return createPondPrivateTensor(applied_function_tensor)
      # operate here

#print("OG:",PPT_to_numpy(x),"\nPiecewise:",vectorized_piecewise(PPT_to_numpy(x)))
#print(piecewise(0.70))
#print(piecewise(PPT_to_numpy(x)))
#for idx,val in enumerate(np.nditer(PPT_to_numpy(x))):
#	print(idx,val)

#a=x.reveal().to_native()
#print(type(x.reveal().to_native()),'\n',x.reveal().decode()[1])

#print(PPT_to_numpy(x),type(PPT_to_numpy(x)),type(x))

#Convert into a numpy array
#print(type(tf.keras.backend.get_value(a)))
#tf.print(tf.Tensor(x,value_index=1,dtype=float))
'''def trySig(x):
	w0 = 0.5
	w1 = 0.2159198015
	w3 = -0.0082176259
	w5 = 0.0001825597
	w7 = -0.0000018848
	w9 = 0.0000000072

	x1 = x
	x2 = x1**2
	x3 = x2 * x
	x5 = x2 * x3
	x7 = x2 * x5
	x9 = x2 * x7

	y1 = x1 * w1
	y3 = x3 * w3
	y5 = x5 * w5
	y7 = x7 * w7
	y9 = x9 * w9

	z = y9 + y7 + y5 + y3 + y1 + w0
	# z = y7 + y5 + y3 + y1 + w0

	return z'''
#print(trySig(2))