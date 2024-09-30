package one.fayaz.fariance.blocks;

import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.core.particles.SimpleParticleType;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.level.block.WallTorchBlock;
import net.minecraft.world.level.block.state.BlockState;

public class CustomWallTorchBlock extends WallTorchBlock {
    public CustomWallTorchBlock(ParticleOptions particleType, Properties properties) {
        super((SimpleParticleType) particleType, properties);
    }

    @Override
    public BlockState getStateForPlacement(BlockPlaceContext context) {
        BlockState state = super.getStateForPlacement(context);
        return state != null ? state : null;
    }
}