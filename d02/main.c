#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>
#include <err.h>
#include <errno.h>

#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
      __typeof__ (b) _b = (b); \
      _a > _b ? _a : _b; })

int valid1(int a, int b, char c, char *pass, char *passEnd) {
    int count = 0;
    for(char *cur = pass; cur <= passEnd; cur++) {
        if(*cur == c) {
            count++;
        }
    }
    return count >= a && count <= b;
}

int valid2(int a, int b, char c, char *pass) {
    return (pass[a-1]==c) ^ (pass[b-1]==c);
}

int main(int argc, char *argv[]) {
    int fd;
    struct stat fs;
    char *buf, *bufend, *cur;
    char c, *pass, *passEnd;
    int r0, r1, res1 = 0, res2 = 0;
    int exitcode = 1, valid = 0;

    if(argc != 2) {
        printf("usage: %s input.txt", argv[0]);
        return 1;
    }

    fd = open(argv[1], O_RDONLY);
    if(fd == -1) {
        err(1, "open: couldn't open the file.");

    }

    if(fstat(fd, &fs) == -1) {
        warn("stat: failed to stat?");
        goto ohcrap;
    }

    buf = cur = mmap(0, fs.st_size, PROT_READ, MAP_SHARED, fd, 0);
    if(buf == (void*) -1) {
        warn("mmap: failed to map file");
        goto ohcrap;
    }

    bufend = buf + fs.st_size;

    while (1) {
        if(cur >= bufend) {
            break;
        }
        // 1-2 c: abcd
        r0 = (int) strtol(cur, &cur, 10);
        cur++;
        r1 = (int) strtol(cur, &cur, 10);
        cur++;

        c = *cur;
        cur++;
        cur++; // get past the colon
        
        pass = ++cur;
        passEnd = memchr(cur, '\n', max(21, bufend - cur));
        res1 += valid1(r0, r1, c, pass, passEnd);
        res2 += valid2(r0, r1, c, pass)?1:0;

        cur = passEnd + 1;
    }

    printf("%d %d\n", res1, res2);

    // all good.
    exitcode = 0;

ohshit:
    munmap(buf, fs.st_size);
ohcrap:
    close(fd);
ohpoop:
    return exitcode;

}