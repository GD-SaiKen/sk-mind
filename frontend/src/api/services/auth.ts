import api from '../client'
import type { LoginParams } from '../types'

export class AuthService {
  private api = api

  async login(data: LoginParams) {
    return this.api.post('/auth/login', data)
  }
}

export const authService = new AuthService()
