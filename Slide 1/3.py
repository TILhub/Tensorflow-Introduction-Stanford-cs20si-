import tensorflow as tf
x=2
y=3
add_op=tf.add(x,y)
mul_op=tf.multiply(x,y)
useless=tf.multiply(x,add_op)
pow_op=tf.pow(add_op,mul_op)
with tf.Session() as sess:
	z=sess.run(pow_op)
	print(z)
#useless tensor is not executed as it is not required by any of the tensors 
#That's the beauty of TensorFlow
