<template>
  <div class="login-page">
    <div class="login-card">
      <div class="login-header">
        <div class="login-logo">AI</div>
        <h2>AI 数据平台</h2>
        <p>企业数据治理与 Agent 服务</p>
      </div>
      <el-form @submit.prevent="handleLogin">
        <el-form-item>
          <el-input
            v-model="form.username"
            placeholder="用户名"
            :prefix-icon="User"
            size="large"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            v-model="form.password"
            type="password"
            placeholder="密码"
            :prefix-icon="Lock"
            show-password
            size="large"
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            :loading="loading"
            native-type="submit"
            size="large"
            class="login-btn"
          >
            登 录
          </el-button>
        </el-form-item>
      </el-form>
      <div class="login-footer">
        <span>默认账号: admin / admin123</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { Lock, User } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';

import { authService } from '@/api';

const router = useRouter();
const form = ref({
  username: 'admin',
  password: 'admin123',
});
const loading = ref(false);

async function handleLogin() {
  loading.value = true;
  try {
    const res = await authService.login(form.value);
    localStorage.setItem('access_token', res.data.access_token);
    ElMessage.success('登录成功');
    router.push('/home');
  } catch {
    /* interceptor handles */
  } finally {
    loading.value = false;
  }
}
</script>

<style lang="scss" scoped>
.login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  width: 400px;
  padding: 40px;
  border-radius: 12px;
  background: $color-bg-white;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.login-header {
  text-align: center;
  margin-bottom: 32px;

  h2 {
    margin: 0 0 4px;
    font-size: $font-size-2xl;
    color: $color-text-primary;
  }

  p {
    margin: 0;
    font-size: $font-size-sm;
    color: $color-text-placeholder;
  }
}

.login-logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  margin-bottom: 12px;
  border-radius: 12px;
  background: linear-gradient(135deg, $color-primary, #337ecc);
  color: $color-bg-white;
  font-size: $font-size-2xl;
  font-weight: $font-weight-bold;
}

.login-btn {
  width: 100%;
}

.login-footer {
  text-align: center;
  margin-top: 20px;
  font-size: 12px;
  color: $color-text-placeholder;
}
</style>
