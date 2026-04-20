import os
from hermes_cli.config import load_config
from hermes_cli.runtime_provider import resolve_runtime_provider, _get_model_config, resolve_requested_provider
from hermes_cli.auth import resolve_provider

print('=== 配置检查 ===')

# 1. 检查配置文件
config = load_config()
print('\n1. 配置文件内容:')
print(f"   Model config: {config.get('model', {})}")

# 2. 检查 _get_model_config
model_cfg = _get_model_config()
print('\n2. _get_model_config 结果:')
print(f"   {model_cfg}")

# 3. 检查 resolve_requested_provider
requested_provider = resolve_requested_provider()
print('\n3. resolve_requested_provider 结果:')
print(f"   {requested_provider}")

# 4. 检查 resolve_provider
try:
    provider = resolve_provider(requested_provider)
    print('\n4. resolve_provider 结果:')
    print(f"   {provider}")
except Exception as e:
    print('\n4. resolve_provider 错误:')
    print(f"   {e}")

# 5. 检查 resolve_runtime_provider
try:
    runtime = resolve_runtime_provider()
    print('\n5. resolve_runtime_provider 结果:')
    print(f"   {runtime}")
except Exception as e:
    print('\n5. resolve_runtime_provider 错误:')
    print(f"   {e}")

# 6. 检查环境变量
print('\n6. 环境变量:')
print(f"   OPENAI_BASE_URL: {os.getenv('OPENAI_BASE_URL')}")
print(f"   OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
print(f"   OPENROUTER_API_KEY: {os.getenv('OPENROUTER_API_KEY')}")