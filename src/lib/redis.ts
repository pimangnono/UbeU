import Redis from 'ioredis';

const getRedisUrl = () => {
    if (process.env.REDIS_URL) {
        return process.env.REDIS_URL;
    }
    // Fallback to localhost for development if not set
    return 'redis://localhost:6379';
};

export const redis = new Redis(getRedisUrl());
