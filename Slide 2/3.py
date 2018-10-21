import tensorflow as tf
# tf.zeros(shape, dtype = tf.float32, name=None)
a= tf.zeros([2,3],tf.int32,'zErO')

# tf.ones(shape, dtype = tf.float32, name=None)

# tf.ones_like(shape, dtype = tf.float32, name=None,optimize=True)

#to general fucntion for above function
# tf.fill(shape,value,name=None)
b=tf.fill([2,6], 89)
with tf.Session() as sess:
	print(sess.run(b))
