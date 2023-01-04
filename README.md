# gcp-cr-pt-api-test

```bash
$ gcloud projects list --sort-by=projectId
```

```bash
$ gcloud config set project [PROJECT_ID]
```

```bash
$ gcloud config get-value project
```

```bash
$ export PROJECT_ID=$(gcloud config get-value project)
```

```bash
$ gcloud config set run/region asia-northeast1
```

```bash
$ gcloud builds submit --project $PROJECT_ID --tag gcr.io/$PROJECT_ID/gcp-cr-pt-api-test
```

```bash
$ gcloud run deploy gcp-cr-pt-api-test \
    --image=gcr.io/$PROJECT_ID/gcp-cr-pt-api-test:latest \
    --platform=managed \
    --concurrency=1 \
    --set-env-vars=MKL_NUM_THREADS=2,OMP_NUM_THREADS=2,NUMEXPR_NUM_THREADS=2 \
    --cpu=2 \
    --memory=1G \
    --allow-unauthenticated \
    --port 8080
```