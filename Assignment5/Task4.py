import sys

def read_int(prompt, default=None):
	while True:
		try:
			s = input(prompt).strip()
			if s == "" and default is not None:
				return int(default)
			return int(s)
		except Exception:
			print("Enter a valid integer")

def read_float(prompt, default=None):
	while True:
		try:
			s = input(prompt).strip()
			if s == "" and default is not None:
				return float(default)
			return float(s)
		except Exception:
			print("Enter a valid number")

def clamp01(x):
	if x != x:
		return 0.0
	if x < 0:
		return 0.0
	if x > 1:
		return 1.0
	return x

def normalize(value, lo, hi):
	try:
		lo = float(lo)
		hi = float(hi)
	except Exception:
		return 0.0
	if hi == lo:
		return 1.0 if value >= hi else 0.0
	return clamp01((value - lo) / (hi - lo))

def interactive():
	print("Create scoring system for applicants")
	n = read_int("Number of features: ")
	features = []
	for i in range(n):
		name = input(f"Feature {i+1} name: ").strip() or f"F{i+1}"
		weight = read_float(f"Weight for '{name}' (positive number): ")
		scale = input(f"Enter scale for '{name}' as min,max (leave empty for 0,100): ").strip()
		if scale:
			try:
				lo, hi = [float(x.strip()) for x in scale.split(",",1)]
			except Exception:
				lo, hi = 0.0, 100.0
		else:
			lo, hi = 0.0, 100.0
		features.append({"name":name,"weight":float(weight),"min":lo,"max":hi})
	m = read_int("Number of applicants: ")
	applicants = []
	for j in range(m):
		aname = input(f"Applicant {j+1} name/ID: ").strip() or f"A{j+1}"
		vals = []
		for f in features:
			v = read_float(f"  {f['name']} value for {aname}: ")
			vals.append(v)
		applicants.append({"id":aname,"values":vals})
	total_weight = sum(f["weight"] for f in features)
	if total_weight == 0:
		print("All weights are zero; cannot compute scores")
		return
	results = []
	for ap in applicants:
		s = 0.0
		for idx,f in enumerate(features):
			norm = normalize(ap["values"][idx], f["min"], f["max"])
			s += f["weight"] * norm
		score_pct = s / total_weight * 100.0
		results.append((ap["id"], round(score_pct,2)))
	results.sort(key=lambda x: x[1], reverse=True)
	print("\nRanking:")
	for rank,(aid,sc) in enumerate(results,1):
		print(f"{rank}. {aid}: {sc}%")

def demo():
	features = [
		{"name":"Experience","weight":3.0,"min":0.0,"max":10.0},
		{"name":"Skills","weight":4.0,"min":0.0,"max":100.0},
		{"name":"Interview","weight":3.0,"min":0.0,"max":10.0},
	]
	applicants = [
		{"id":"Alice","values":[6,85,8]},
		{"id":"Bob","values":[8,70,7]},
		{"id":"Carol","values":[4,95,9]},
	]
	total_weight = sum(f["weight"] for f in features)
	results = []
	for ap in applicants:
		s = 0.0
		for idx,f in enumerate(features):
			norm = normalize(ap["values"][idx], f["min"], f["max"])
			s += f["weight"] * norm
		results.append((ap["id"], round(s/total_weight*100.0,2)))
	results.sort(key=lambda x: x[1], reverse=True)
	print("Demo features and weights:")
	for f in features:
		print(f" - {f['name']}: weight={f['weight']} scale=({f['min']},{f['max']})")
	print("\nDemo applicants and scores:")
	for rank,(aid,sc) in enumerate(results,1):
		print(f"{rank}. {aid}: {sc}%")

def main():
	if "--demo" in sys.argv:
		demo()
	else:
		interactive()

if __name__ == "__main__":
	main()
