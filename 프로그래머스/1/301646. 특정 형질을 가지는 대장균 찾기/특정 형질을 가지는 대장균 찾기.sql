SELECT COUNT(ID) COUNT
FROM ECOLI_DATA 
WHERE 
    CONV(GENOTYPE, 10, 2) NOT LIKE '%1_' AND
    (CONV(GENOTYPE, 10, 2) LIKE '%1' OR
    CONV(GENOTYPE, 10, 2) LIKE '%1__')
    
-- CONV함수를 사용해 10진수 숫자를 2진수로 변환한다.
-- LIKE 함수를 사용해서 2번 형질이 없는 경우 '%1_',
-- 1번 형질을 보유한 경우 '%1', 3번 형질을 보유한 경우 '%1__'로 문자열을 비교한다.