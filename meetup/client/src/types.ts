interface UserBase {
	first_name: string;
	last_name: string;
	username: string;
}

interface User extends UserBase {
	id: number;
	is_active: boolean;

	meets: Meet[];

	registered_in_telegram: boolean;
	telegram_chat_id?: number;
}

interface UserCreate extends UserBase {
	password: string;
}

interface UserLogin {
	username: string;
	password: string;
}

interface MeetBase {
	name: string;
	description: string;
	start_at: string;
	members?: User[];
}

interface Meet extends MeetBase {
	creator?: User;
	id: number;
	created: string;
}

interface MeetCreate {
	name: string;
	description: string;
	start_at: Date;
	members_usernames: string[];
	creator_id: number;
}

export type { User, UserCreate, UserLogin, Meet, MeetCreate };
