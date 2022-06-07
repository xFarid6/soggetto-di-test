# include <iostream>

int words_distance_levenshtein(const char *s1, const char *s2)
{
    const int len1 = strlen(s1);
    const int len2 = strlen(s2);
    int d[len1 + 1][len2 + 1];
    int i, j;

    for (i = 0; i <= len1; i++)
        d[i][0] = i;
    for (j = 0; j <= len2; j++)
        d[0][j] = j;

    for (i = 1; i <= len1; i++)
        for (j = 1; j <= len2; j++)
            d[i][j] = std::min(d[i - 1][j] + 1, std::min(d[i][j - 1] + 1, d[i - 1][j - 1] + (s1[i - 1] == s2[j - 1] ? 0 : 1)));

    return d[len1][len2];
}


int words_distance_levenshtein_recursive(const char *s1, const char *s2)
{
    const int len1 = strlen(s1);
    const int len2 = strlen(s2);
    int d[len1 + 1][len2 + 1];
    int i, j;

    for (i = 0; i <= len1; i++)
        d[i][0] = i;
    for (j = 0; j <= len2; j++)
        d[0][j] = j;

    for (i = 1; i <= len1; i++)
        for (j = 1; j <= len2; j++)
            d[i][j] = std::min(d[i - 1][j] + 1, std::min(d[i][j - 1] + 1, d[i - 1][j - 1] + (s1[i - 1] == s2[j - 1] ? 0 : 1)));

    return d[len1][len2];
}

int words_distance_levenshtein_recursive_memo(const char *s1, const char *s2)
{
    const int len1 = strlen(s1);
    const int len2 = strlen(s2);
    int d[len1 + 1][len2 + 1];
    int i, j;

    for (i = 0; i <= len1; i++)
        d[i][0] = i;
    for (j = 0; j <= len2; j++)
        d[0][j] = j;

    for (i = 1; i <= len1; i++)
        for (j = 1; j <= len2; j++)
            d[i][j] = std::min(d[i - 1][j] + 1, std::min(d[i][j - 1] + 1, d[i - 1][j - 1] + (s1[i - 1] == s2[j - 1] ? 0 : 1)));

    return d[len1][len2];
}
