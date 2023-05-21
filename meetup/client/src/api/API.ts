import axios, { AxiosResponse } from "axios";
import { Meet, MeetCreate, User, UserCreate, UserLogin } from "../types";
import {
	BaseResponse,
	CurrentActiveUserPayload,
	CurrentActiveUserResponse,
	MeetResponse,
	MeetsResponse,
	UserResponse,
	UsersResponse,
} from "./responses";
class API {
	private static domain = "http://localhost:8000";
	private static APIEndpoints = {
		GetUsers: `${this.domain}/users`,
		GetCurrentActiveUser: `${this.domain}/users/current`,
		CreateUser: `${this.domain}/users`,
		CreateMeet: `${this.domain}/meets`,
		LoginUser: `${this.domain}/auth/login`,
		logoutCurrentUser: `${this.domain}/auth/logout`,
		GetCurrentActiveUserMeets: `${this.domain}/meets/current_active_user`,
	};

	public static createUser = async (userData: UserCreate): Promise<boolean> => {
		try {
			const { data }: AxiosResponse<UserResponse> = await axios.post(
				this.APIEndpoints.CreateUser,
				userData
			);
			return data.success;
		} catch (error) {
			console.log(error);
			return false;
		}
	};

	public static createMeet = async (
		meetData: MeetCreate
	): Promise<Meet | undefined> => {
		try {
			const { data }: AxiosResponse<MeetResponse> = await axios.post(
				this.APIEndpoints.CreateMeet,
				meetData,
				{ withCredentials: true }
			);
			return data.payload.meet;
		} catch (error) {
			return;
		}
	};

	public static loginUser = async ({
		username,
		password,
	}: UserLogin): Promise<boolean> => {
		const formData = new FormData();
		formData.append("username", username);
		formData.append("password", password);
		try {
			const { data }: AxiosResponse<BaseResponse> = await axios.post(
				this.APIEndpoints.LoginUser,
				formData,
				{
					withCredentials: true,
				}
			);
			return data.success;
		} catch (error) {
			return false;
		}
	};
	public static logoutCurrentUser = async (): Promise<boolean> => {
		try {
			const { data }: AxiosResponse<BaseResponse> = await axios.get(
				this.APIEndpoints.logoutCurrentUser,
				{ withCredentials: true }
			);
			return data.success;
		} catch (error) {
			return false;
		}
	};

	public static getCurrentActiveUser =
		async (): Promise<CurrentActiveUserPayload> => {
			try {
				const { data }: AxiosResponse<CurrentActiveUserResponse> =
					await axios.get(this.APIEndpoints.GetCurrentActiveUser, {
						withCredentials: true,
					});
				return data.payload;
			} catch (error) {
				const payload: CurrentActiveUserPayload = {
					user: undefined,
					authenticated: false,
				};
				return payload;
			}
		};

	public static getUsers = async (): Promise<User[]> => {
		try {
			const { data }: AxiosResponse<UsersResponse> = await axios.get(
				this.APIEndpoints.GetUsers,
				{ withCredentials: true }
			);
			return data.payload.users;
		} catch (error) {
			return [];
		}
	};

	public static getCurrentActiveUserMeets = async (): Promise<Meet[]> => {
		try {
			const { data }: AxiosResponse<MeetsResponse> = await axios.get(
				this.APIEndpoints.GetCurrentActiveUserMeets,
				{
					withCredentials: true,
				}
			);
			const { meets } = data.payload;
			if (Array.isArray(meets)) return meets;
			else return [];
		} catch (error) {
			return [];
		}
	};
}

export default API;
