const URLs = {
	Home: "/",
	Login: "/login",
	Registration: "/sign-in",
	PersonalCabinet: (username: string): string => {
		return `/users/${username}`;
	},
	PersonalCabinetUrlPattern: "/users/:username",
};

export default URLs;
