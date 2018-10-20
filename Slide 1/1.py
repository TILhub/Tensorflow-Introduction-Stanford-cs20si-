import tensorflow as tf
x=3
y=4
a=tf.add(3,4)
#both  statements are same
#a=tf.add(x,y)
print(a)
#no processing till here
#prints information about tensor a
sess=tf.Session()
print(sess.run(a))
#process is created here 
sess.close()
#it is important to release all resorces
