import math

def solution(fees, records):
    # 주차 기록을 저장할 딕셔너리
    parking_records = {}
    total_time = {}
    
    # 입출차 기록을 파싱하여 저장
    for record in records:
        time, car_number, inont = record.split()
        if inont == 'IN':
            # 입차 기록을 추가
            parking_records[car_number] = time
        else:
            # 출차 시 누적 주차 시간 계산
            in_time = parking_records.pop(car_number)
            parked_minutes = time_to_minute(in_time, time)
            total_time[car_number] = total_time.get(car_number, 0) + parked_minutes

    # 입차 후 출차 기록이 없는 경우, 출차를 23:59로 가정
    for car_number, in_time in parking_records.items():
        parked_minutes = time_to_minute(in_time, "23:59")
        total_time[car_number] = total_time.get(car_number, 0) + parked_minutes
    
    # 요금 계산
    result = []
    for car_number in sorted(total_time.keys()):
        parked_minutes = total_time[car_number]
        result.append(calculate_fee(parked_minutes, fees))
    
    return result

def time_to_minute(in_time, out_time):
    out_h, out_m = map(int, out_time.split(':'))
    in_h, in_m = map(int, in_time.split(':'))
    return (out_h * 60 + out_m) - (in_h * 60 + in_m)

def calculate_fee(minutes, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    # 주차시간이 기본시간보다 작거나 같으면 기본 요금 반환
    if minutes <= basic_time:
        return basic_fee
    else:
        # 초과 시간 계산 및 올림 처리
        return basic_fee + math.ceil((minutes - basic_time) / unit_time) * unit_fee
