import { Meet, User } from "../types";

interface BaseResponse {
	msg: string;
	success: boolean;
	status_code: number;
	payload: object;
}

interface GetCurrentActiveUserResponse extends BaseResponse {
	payload: GetCurrentActiveUserPayload;
}

interface GetUsersResponse extends BaseResponse {
	payload: GetUsersPayload;
}

interface GetUserResponse extends BaseResponse {
	payload: GetUserPayload;
}

interface GetMeetsResponse extends BaseResponse {
	payload: GetMeetsPayload;
}
interface GetMeetResponse extends BaseResponse {
	payload: GetMeetPayload;
}

interface GetMeetPayload {
	meet: Meet;
}

interface GetMeetsPayload {
	meets?: Meet[];
}

interface GetCurrentActiveUserPayload {
	user?: User;
	authenticated: boolean;
}

interface GetUsersPayload {
	users: User[];
}

interface GetUserPayload {
	user: User;
}

export type {
	GetMeetsResponse,
	GetMeetResponse,
	BaseResponse,
	GetCurrentActiveUserResponse,
	GetCurrentActiveUserPayload,
	GetUsersResponse,
	GetUsersPayload,
	GetUserResponse,
};
