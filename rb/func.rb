def iamafunction(para1,para2)
	puts"the first argument was #{para1}  ,and the second is #{para2}"
	
end


def addition(x,y)
	x+y
end

def subtraction(first,second)
	while second !=0
		first-=1
		second -=1
	end
	first
end

def sub_recursive(f,s)
	if s!=0
		sub_recursive(f-1,s-1)
	end
	f
end

puts addition(3,5)
puts subtraction(12,5)
puts sub_recursive(27,14)
puts iamafunction("wangheng",'tyraan')