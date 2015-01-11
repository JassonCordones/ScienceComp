
def sqrt2(x, debug=False):
	s = 1.
	kmax = 100
	tol = 1e-14
	for k in range(6):
		if debug:
			print ("Before iteration %s, s = %20.15f" % (k+1,s))
		s0 = s
		s = 0.5*(s + x/s)
		delta_s = s-s0
		if abs(delta_s / x) < tol:
			break
	if debug:
		print ("After %s iterations, s = %20.15f" % (k+1,s))
	return s