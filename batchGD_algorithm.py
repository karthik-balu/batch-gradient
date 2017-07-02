def hypothesis(theta0,theta1,x):
	h = theta0 + (x*theta1)
	return int(round(h))

def costfunction(theta0,theta1,x,y,number_cases):
	sumvalue = 0
	for i in range(number_cases):
		plaindiff = hypothesis(theta0,theta1,x[i]) - y[i]
		sumvalue = sumvalue + (plaindiff**2)
	j = sumvalue / (2*number_cases) ;
	return j

def main():
	print("Enter number of input cases")
	number_cases = input()
	x = []
	y = []
	for i in range(number_cases):
		#print("Enter House size")
		x.append(i+1)
		#print("Enter House price")
		y.append(i+1)
	#print(costfunction(0,0,x,y,number_cases))
	val = grad_descent(0,0,x,y,number_cases)
	while(True):
		print("Enter your house size")	
		i = input()
		if(i == 0):
			break
		else:
			print("Your house price should be:",hypothesis(val[0],val[1],i))

def newt0(number_cases,theta0,theta1,x,y):
	sumvalue = 0
	for i in range(number_cases):
		print("hyp is" ,hypothesis(theta0,theta1,x[i]))
		plaindiff = hypothesis(theta0,theta1,x[i]) - y[i]
		sumvalue = sumvalue + plaindiff
	t0 = sumvalue / number_cases ;
	return t0

def newt1(number_cases,theta0,theta1,x,y):
	sumvalue = 0
	for i in range(number_cases):
		plaindiff = hypothesis(theta0,theta1,x[i]) - y[i]
		sumvalue = sumvalue + (plaindiff*x[i])
	t1 = sumvalue / number_cases ;
	return t1

def grad_descent(theta0,theta1,x,y,number_cases):
	temp0 = theta0 - 0.001*newt0(number_cases,theta0,theta1,x,y)
	temp1 = theta1 - 0.001*newt1(number_cases,theta0,theta1,x,y)
	newtheta0 = temp0
	newtheta1 = temp1
	print(newtheta0,newtheta1)
	#print(costfunction(newtheta0,newtheta1,x,y,number_cases))
	#print(costfunction(theta0,theta1,x,y,number_cases))
	if(newtheta0==theta0)and(newtheta1==theta1):
		val = (newtheta0,newtheta1)
		ret = list(val)
		print ret
		return ret 
	else:
		return grad_descent(newtheta0,newtheta1,x,y,number_cases)
	

if __name__=="__main__":
	main()


