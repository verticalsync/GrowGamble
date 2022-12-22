from misc.variables import emojis


def isalnum(string: str) -> bool:
	char_list = "qwertyuiopasdfghjklzxcvbnm1234567890"

	for char in string.lower():
		if char not in char_list:
			return False
	return True


def parse_world_locks(world_locks: int) -> tuple[int, int, int, int]:
	dirts = 0
	bgls = 0
	dls = 0
	wls = 0
	if world_locks < 0:
		world_locks = 0
	while world_locks != 0:
		if world_locks > 1999999:
			dirts += 2
			world_locks -= 2000000
		if world_locks > 19999:
			bgls += 2
			world_locks -= 20000
		elif world_locks > 199:
			dls += 2
			world_locks -= 200
		else:
			wls += world_locks
			world_locks = 0
	return dirts, bgls, dls, wls


def create_balance_message(dirts: int, bgls: int, dls: int, wls: int) -> str:
	bal = ""
	if dirts != 0:
		bal += f"{dirts} {emojis['dirt']} "
	if bgls != 0:
		bal += f"{bgls} {emojis['blue_gem_lock']} "
	if dls != 0:
		bal += f"{dls} {emojis['diamond_lock']} "
	if wls != 0:
		bal += f"{wls} {emojis['world_lock']}"
	if bal == "":
		bal = f"0 {emojis['world_lock']}"
	return bal
