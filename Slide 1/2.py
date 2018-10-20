import tensorflow as tf
x=2
y=3
op1=tf.add(x,y)
op2=tf.multiply(x,y)
op3=tf.pow(op1,op2)
with tf.Session() as sess:
	op=sess.run(op3)
	print(op)
	
