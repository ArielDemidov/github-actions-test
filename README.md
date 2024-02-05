# github-actions-test

Running the following command on WSL Kali-linux:

```bash
echo "S3_BUCKET_NAME=$(terraform output -raw aws_s3_bucket | tr -d '"')" >> test.txt
```

yields me with a txt file containing: 
```
S3_BUCKET_NAME=test-eladbe-test

```

## What's weird with that?<br>
There's a newline in the end of the string

At build #15 I figured out that maybe there are newline hidden characters which may break the GITHUB_ENV file, so I added the `-raw` to the terraform output command in the next job (#16) and got the following output:

`Invalid format 'test-eladbe-test::debug::Terraform exited with code 0.'`

We can clearly see that Terraform is adding some garbage to our output<br>
This leads me to believe that when we ran 
```bash
echo "S3_BUCKET_NAME=$(terraform output -raw aws_s3_bucket | tr -d '"')" >> $GITHUB_ENV
```
then GITHUB_ENV got injected with some _trash_ Terraform debug logs, which in turn, broke it.<br>

Apperantly, when appending 1 out of place character into GITHUB_ENV then it eats shit and exits. For some reason only the last valid line is outputted which makes debugging really fucking difficult.

Eventually apperantly you need to disable the `terraform_wrapper` by adding these lines to the github actions under `uses: hashicorp/setup-terraform@v1`:

```yml
        with:
          terraform_wrapper: false
```

Here's a more detailed StackOverflow answer regarding this finnicky behaviour: 
https://stackoverflow.com/questions/69925970/how-to-save-terraform-output-variable-into-a-github-action-s-environment-variabl