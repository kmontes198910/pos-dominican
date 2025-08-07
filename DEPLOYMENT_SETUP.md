# 🚀 ERP Medinec CI/CD Pipeline Setup

This repository contains an enterprise-grade GitHub Actions workflow that provides a complete CI/CD pipeline with automated testing, Docker image building, and Kubernetes deployment.

## 📋 Pipeline Overview

Our CI/CD pipeline implements a **three-stage architecture**:

### 🧪 Stage 1: Validation & Testing
- Automated code change detection
- Comprehensive test execution
- Test artifact generation and storage
- Pull request validation

### 🔨 Stage 2: Build & Publish Docker Image
- Multi-platform Docker builds (AMD64/ARM64)
- Semantic versioning based on branch
- Docker layer caching for optimal performance
- Multi-tag image publishing
- Optional security scanning

### 🚢 Stage 3: Deploy to Kubernetes
- Environment-aware deployments
- Secure VPN connectivity
- Pre-deployment validation
- Rolling updates with health checks
- Post-deployment verification

## 🔐 Required GitHub Secrets

Configure these secrets in your repository: `Settings > Secrets and variables > Actions`

### 📦 Container Registry Secrets
```yaml
DOCKER_HUB_USERNAME     # Your Docker Hub username
DOCKER_HUB_PASSWORD     # Docker Hub access token
PACKAGE_TOKEN          # GitHub Package token (if needed)
```

### 🔒 VPN Connection Secrets
```yaml
VPN_CONFIG             # Complete .ovpn file content
VPN_USERNAME           # VPN username (e.g., "cicd")
VPN_PASSWORD           # VPN password
```

### ⚙️ Kubernetes Access Secrets
```yaml
K8S_CLUSTER_IP         # Cluster IP (e.g., "10.1.0.10")
KUBE_CONFIG_DEV        # Base64 encoded kubeconfig for development
KUBE_CONFIG_STAGING    # Base64 encoded kubeconfig for staging
KUBE_CONFIG_PROD       # Base64 encoded kubeconfig for production
```

### 📝 How to Encode Kubeconfig
```bash
# Encode your kubeconfig file:
cat ~/.kube/config | base64 -w 0

# Or for specific environment:
cat ~/.kube/config-dev | base64 -w 0
```

## 🎯 Workflow Triggers

The pipeline automatically triggers on:

### 🔄 Automatic Triggers
- **Push to main branches**: `master`, `main`, `develop`
- **Pull Requests**: Validation and testing only
- **Path filtering**: Ignores documentation-only changes

### 🎛️ Manual Triggers
Workflow dispatch with options:
- **Target Environment**: development, staging, production
- **Force Rebuild**: Ignore Docker cache
- **Skip Tests**: Fast deployment option

## 🏗️ Environment Configuration

The workflow supports multiple environments with automatic detection:

| Branch | Environment | Namespace | Version Format |
|--------|-------------|-----------|----------------|
| `master`/`main` | production | `kynsoft-prod` | `v1.0.YYYYMMDDHHMMSS` |
| `develop` | development | `kynsoft-dev` | `v0.9.YYYYMMDDHHMMSS-dev` |
| Other branches | staging | `kynsoft-staging` | `v0.8.YYYYMMDDHHMMSS-branch` |

## 🔧 Customization Guide

### 📝 Service Configuration
Update these variables in the workflow file:

```yaml
env:
  # Application Settings
  SERVICE_NAME: 'erp-medinec'                    # Your service name
  SERVICE_PATH: '.'                              # Path to Dockerfile
  DOCKER_IMAGE_NAME: 'erp-medinec'              # Docker image name
  
  # Kubernetes Settings
  K8S_DEPLOYMENT_NAME: 'erp-medinec-deployment' # K8s deployment name
  K8S_CONTAINER_NAME: 'erp-medinec-container'   # Container name in deployment
  K8S_SERVICE_NAME: 'erp-medinec-service'       # K8s service name
  
  # Performance Settings
  DEPLOYMENT_TIMEOUT: '600s'                    # Deployment timeout
  HEALTH_CHECK_RETRIES: 5                       # Health check attempts
```

### 🧪 Test Configuration
Customize the testing steps:

```yaml
- name: 🧪 Run Tests
  run: |
    # Add your specific test commands:
    # npm test                    # Node.js
    # python -m pytest           # Python
    # go test ./...              # Go
    # mvn test                   # Java Maven
    # ./gradlew test             # Java Gradle
```

## 🏷️ Image Tagging Strategy

Images are automatically tagged with:
- `latest` (for main branch)
- `v1.0.YYYYMMDDHHMMSS` (semantic version)
- `branch-COMMIT_SHA` (branch-specific)
- `branch-latest` (latest for branch)

## 🛡️ Security Features

### 🔐 Security Best Practices
- ✅ Secure file permissions (600) for sensitive files
- ✅ Automatic cleanup of credentials after use
- ✅ VPN connection with timeout and retry logic
- ✅ Base64 encoded kubeconfig storage
- ✅ Optional container image security scanning

### 🚨 Security Scanning (Optional)
Uncomment in the workflow to enable:
```yaml
# Add security scanning with Trivy
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image ${{ steps.meta.outputs.tags }}
```

## 📊 Monitoring & Observability

### 📈 Built-in Monitoring
- ✅ Detailed deployment progress tracking
- ✅ Pod health verification
- ✅ Service status monitoring
- ✅ Event log analysis
- ✅ Rollout status confirmation

### 🔍 Health Checks
- Pre-deployment validation
- Post-deployment verification
- Pod readiness confirmation
- Service availability checks

### 📋 Deployment Summary
Each successful deployment provides:
- 📦 Image details and registry links
- 🌍 Environment and namespace info
- 🕒 Deployment timestamp
- 👤 Triggering user information
- 🔗 Quick access links

## 🚀 Getting Started

### 1️⃣ Prerequisites Checklist
- [ ] `Dockerfile` in repository root
- [ ] Kubernetes deployment created in cluster
- [ ] Docker Hub account and repository
- [ ] OpenVPN configuration file
- [ ] Valid kubeconfig for each environment
- [ ] All GitHub secrets configured

### 2️⃣ Initial Setup
1. **Copy the workflow file** to `.github/workflows/deploy.yml`
2. **Configure GitHub secrets** (see secrets section above)
3. **Customize environment variables** in the workflow
4. **Update test commands** for your tech stack
5. **Verify Kubernetes deployment** exists in target cluster

### 3️⃣ First Deployment
1. **Push to main branch** or trigger manually
2. **Monitor workflow** in GitHub Actions tab
3. **Verify deployment** in Kubernetes cluster
4. **Check application** availability

## 🔧 Advanced Configuration

### 🔄 Cache Optimization
The workflow uses multiple cache strategies:
- GitHub Actions cache for Docker layers
- Registry-based cache for build optimization
- Dependency caching for faster builds

### 🌍 Multi-Environment Support
```yaml
# Environment-specific configurations
production:
  namespace: kynsoft-prod
  replicas: 3
  resources: high
  
development:
  namespace: kynsoft-dev
  replicas: 1
  resources: low
```

### 📬 Notification Integration
Add notification support (uncomment and configure):
```yaml
# Slack notification
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Deployment completed!"}' \
  ${{ secrets.SLACK_WEBHOOK_URL }}

# Microsoft Teams
curl -H "Content-Type: application/json" \
  -d '{"text":"Deployment status"}' \
  ${{ secrets.TEAMS_WEBHOOK_URL }}
```

## 🐛 Troubleshooting Guide

### ❌ Common Issues

| Issue | Solution |
|-------|----------|
| VPN connection fails | Verify VPN_CONFIG, VPN_USERNAME, VPN_PASSWORD secrets |
| kubectl access denied | Check KUBE_CONFIG_* secrets are base64 encoded correctly |
| Deployment not found | Ensure K8S_DEPLOYMENT_NAME matches actual deployment |
| Image pull fails | Verify Docker Hub credentials and image name |
| Timeout during deployment | Increase DEPLOYMENT_TIMEOUT or check cluster resources |

### 🔍 Debug Commands
```bash
# Check VPN connection locally
sudo openvpn --config your-config.ovpn --auth-user-pass auth.txt

# Verify kubeconfig encoding
echo "YOUR_BASE64_KUBECONFIG" | base64 -d | kubectl --kubeconfig=/dev/stdin get nodes

# Test Docker image locally
docker run --rm your-username/erp-medinec:latest
```

### 📱 Monitoring Deployment
- **GitHub Actions**: Monitor workflow progress and logs
- **Kubernetes Dashboard**: View deployment status and pod health
- **Application Logs**: Check pod logs for application-specific issues
- **VPN Logs**: Review VPN connection logs in case of connectivity issues

## 🔄 Maintenance

### 📅 Regular Tasks
- [ ] Update workflow dependencies monthly
- [ ] Rotate VPN and registry credentials quarterly
- [ ] Review and update kubeconfig annually
- [ ] Monitor Docker image sizes and optimize
- [ ] Update security scanning tools

### 🚀 Performance Optimization
- Use multi-stage Dockerfile for smaller images
- Implement proper Docker layer caching
- Optimize test execution time
- Configure resource limits appropriately

## 🆘 Support

For issues and questions:
1. **Check workflow logs** in GitHub Actions
2. **Review this documentation** for configuration
3. **Verify all prerequisites** are met
4. **Test components individually** (VPN, kubectl, Docker)
5. **Contact DevOps team** for cluster-specific issues

---

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Build Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Deployment Guide](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [OpenVPN Configuration Guide](https://openvpn.net/community-resources/)

**Happy Deploying! 🚀**
