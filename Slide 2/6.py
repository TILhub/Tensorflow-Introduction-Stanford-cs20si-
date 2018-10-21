import tensorflow as tf

W=tf.Variable(10)
W.assign(1000)
with tf.Session() as sess:
	sess.run(W.initializer)
	print(W.eval()) #dafaq
	
	# assign operation need to be executed to take its effect



	# correct way to do it
	
with tf.Session() as sess:
	assign_op=W.assign(100)
	sess.run(W.initializer)
	sess.run(assign_op)
	print(sess.run(W))
