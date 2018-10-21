import tensorflow as tf

a=tf.constant([2,2], name='a')

b=tf.constant([[0,1],[2,3]],name='b')

x=tf.multiply(a,b,name='MUL')
# this is not a matrix multiplication 
# rather it is a row elemnt wise muktiplcation
# run the program to see what I am talking about
with tf.Session() as sess:
	print(sess.run(x))

