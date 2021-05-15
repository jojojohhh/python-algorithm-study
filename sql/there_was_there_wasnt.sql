SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS AS INS, ANIMAL_OUTS AS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID AND INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME