#!/bin/bash

#관리노드에서 실행
repolist="baseos appstream"
repopath=/repo

for repo in $repolist; do
  reposync --download-metadata --repo=$repo -p $repopath
done

