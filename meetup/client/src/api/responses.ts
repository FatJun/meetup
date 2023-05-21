import { Meet, User } from "../types";

export interface BaseResponse {
	msg: string;
	success: boolean;
	status_code: number;
	payload: object;
}

export interface CurrentActiveUserResponse extends BaseResponse {
	payload: CurrentActiveUserPayload;
}

export interface UsersResponse extends BaseResponse {
	payload: UsersPayload;
}

export interface UserResponse extends BaseResponse {
	payload: UserPayload;
}

export interface MeetsResponse extends BaseResponse {
	payload: MeetsPayload;
}
export interface MeetResponse extends BaseResponse {
	payload: MeetPayload;
}

export interface MeetPayload {
	meet: Meet;
}

export interface MeetsPayload {
	meets?: Meet[];
}

export interface CurrentActiveUserPayload {
	user?: User;
	authenticated: boolean;
}

export interface UsersPayload {
	users: User[];
}

export interface UserPayload {
	user: User;
}
